- [clustering](#clustering)
- [coordinates](#coordinates)
- [webscraper](#webscraper)
- [index](#index)


# My Capstone Research Project: Creating a Predictive Model for Potential Hazardous Locations
SOAP(Students Organized Against Pollution)

Christopher Smith
SOAP Capstone Project

Here are some python files I've created for my Capstone Research Project. The goal of the project was to identify locations that could be brownfields, which are sites that are environmentally compromised. They're usually sites that used to be previously owned by factories. If you would like to learn more, I included my research paper in the docs folder.

A description is given for each file listed. An example of front end development with HTML and javascript is found in index.htm. 

# clustering 
clustering.py

## Description
This file uses DBSCAN which is a python library which creates clusters(groupings) out of given data. My code implements this algorithm to create a yellow cluster which is a grouping for potentially contaminated areas and a red cluster which is a different grouping for likely contaminated areas.

## Dependencies 
Install scikit learn library which contains DBSCAN ```pip install -U scikit-learn```

## Output
Screenshot of output where locations are plotted by their longitude and latitude coordinates. The red circles represent the likely contaminated areas and the yellow circles represent potentially contaminated areas.

![Image of Clustering](https://github.com/TCNJsmithc69/My-Capstone-Research-Project/blob/main/images/clusteringAlgorithm.PNG)

# coordinates
(coordinates.py)

## Description
This file uses the geopy library to convert addresses into a geolocation with x and y coordinates.

## Dependencies 
Download geopy library with ```pip install geopy```

# webscraper
webscraper.py

## Description
A combined webscraper and crawler that uses selenium to navigate to active contaminated sites on the NJDEP website for Trenton locations. Once it navigates to a specific page, addresses for each site in the Trenton area are stored in a file named addresses.csv.

## Dependencies 
Download selenium with the command  ```sudo pip install selenium```

Download pandas with the command ```pip install pandas```

Download chrome driver with associated with your chrome version at https://chromedriver.chromium.org/downloads
# index
index.htm

## Description
Html page that can be hosted on localhost that uses the javascript library leaflet which is a mapping tool. Using the longitude and latitude coordinates that were converted with coordinates.py, each brownfield location is displayed using OpenStreetMap. Also, cluster groups are shown using yellow(potentially contaminated) and red(likely contaminated) zones.

## Dependencies 
To run this file use the command  ```python -m http.server``` after downloading a stable version of leaflet at https://leafletjs.com/download.html

## Output
Screenshot of output for OpenStreetMap locations.
![Image of OpenStreetMaps](https://github.com/TCNJsmithc69/My-Capstone-Research-Project/blob/main/images/clustersScreenshot.PNG)


