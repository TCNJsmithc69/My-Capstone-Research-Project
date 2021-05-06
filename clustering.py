'''
Christopher Smith

This script is used to create clusters using the DBSCAN(density-based spatial clustering of applications) implementation
Creates two different types of clusters which are labeled as the yellow and redclusters. The yellow cluster covers areas
that are potentially contaminated. The red cluster covers areas that are likely to be contaminated. The results are 
displayed in a diagram that uses matplotlib 

'''



import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from geopy.distance import great_circle
from shapely.geometry import MultiPoint


#yellow cluster function that returns the centroid of each cluster as centermost_point
def get_centermost_point(cluster):
    try:
        centroid = (MultiPoint(cluster).centroid.x, MultiPoint(cluster).centroid.y)
    except IndexError:
        return
    centroid = (MultiPoint(cluster).centroid.x, MultiPoint(cluster).centroid.y)
    centermost_point = min(cluster, key=lambda point: great_circle(point, centroid).m)
   
    return tuple(centermost_point)
  

#red cluster function that returns the centroid of each cluster as centermost_point
def get_centermost_point2(cluster2):
    centroid2 = (MultiPoint(cluster2).centroid.x, MultiPoint(cluster2).centroid.y)
    centermost_point2 = min(cluster2, key=lambda point: great_circle(point, centroid2).m)
    return tuple(centermost_point2)


def clustering(df):

    #covert latitude and longitude columns in dataframe to a numpy array
    coords = df[['Lat','Lon']].to_numpy()
    kms_per_radian = 6371.0088
    #set the radius of the cluster to 200 meters
    epsilon = .2 / kms_per_radian
    #use the ball_tree algorithm which works in O(nlog(n)) time with a minimum samples of 1
    db = DBSCAN(eps=epsilon, min_samples=1, algorithm='ball_tree', metric='haversine').fit(np.radians(coords))
    cluster_labels = db.labels_
    #count the number of clusters
    num_clusters = len(set(cluster_labels))
    #create a series which is a column of coordinates
    clusters = pd.Series([coords[cluster_labels == n] for n in range(num_clusters)])
    #print the number of clusters
    print('Number of clusters: {}'.format(num_clusters))
    #do the same for the red clusters with a minium samples of 3
    db2 = DBSCAN(eps=epsilon, min_samples=3, algorithm='ball_tree', metric='haversine').fit(np.radians(coords))
    cluster_labels2 = db2.labels_
    num_clusters2 = len(set(cluster_labels2))
    clusters2 = pd.Series([coords[cluster_labels2 == n] for n in range(num_clusters2)])
    #print the number of clusters
    print('Number of clusters: {}'.format(num_clusters2))


    #yellow area
    centermost_points = clusters.map(get_centermost_point)
    #collect the centroids of all clusters in the yellow area and record their latitude and longitude coordinates
    lats, lons = zip(*centermost_points)
    #create a dataframe with longitude and latitude columns
    rep_points = pd.DataFrame({'Lon':lons, 'Lat':lats})
    rs = rep_points.apply(lambda row: df[(df['Lat']==row['Lat']) & (df['Lon']==row['Lon'])].iloc[0], axis=1)
    #store as a csv file
    rs.to_csv('data/red_clusters.csv', index=False)

    #red area
    centermost_points2 = clusters2.map(get_centermost_point)
    #drop all null values
    centermost_points2 = centermost_points2.dropna()
     #collect the centroids of all clusters in the red area and record their latitude and longitude coordinates
    lats, lons = zip(*centermost_points2)
    rep_points = pd.DataFrame({'Lon':lons, 'Lat':lats})
    rs2 = rep_points.apply(lambda row: df[(df['Lat']==row['Lat']) & (df['Lon']==row['Lon'])].iloc[0], axis=1)
    rs2.to_csv('data/yellow_clusters.csv', index=False)

    #plot the data using matplotlib
    fig, ax = plt.subplots(figsize=[10, 6])

    yellow_scatter = ax.scatter(rs['Lon'], rs['Lat'], c='#ffff00', edgecolor='None', alpha=0.7, s=3000)
    red_scatter = ax.scatter(rs2['Lon'], rs2['Lat'], c='#ff0000', edgecolor='None', alpha=0.7, s=3000) 
    df_scatter = ax.scatter(df['Lon'], df['Lat'], c='k', alpha=0.9, s=3)
    ax.set_title('DBSCAN areas')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    plt.show()

#read in coordinates csv file
df = pd.read_csv('data/coordinates.csv')
clustering(df)

