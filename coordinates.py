'''
Christopher Smith

This script is used to convert addresses given by the addresses.csv file into 
a geolocation which consists of a latitude and longitude coordinate

Uses geopy and pandas libraries  
'''

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import pandas as pd

def converter(df):  
    #choose geocoder
    geolocator = Nominatim(user_agent="myGeocoder")
    #convert address into a location, delay is used so the agent does not kick out the user
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    #Save as location column in dataframe
    df['location'] = df['Address'].apply(geocode)
    #Save as latitude column in dataframe
    df['Lat'] = df['location'].apply(lambda x: x.latitude if x else None)
    #Save as longitude column in dataframe
    df['Lon'] = df['location'].apply(lambda x: x.longitude if x else None)
    #Drop location column since it is not needed
    df=df.dropna(subset=['location'])
    #Save as a csv file
    df.to_csv('data/coordinates.csv', index=False)

#Choose input file to gather addresses
df = pd.read_csv("data/addresses.csv")
converter(df)

