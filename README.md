# My-Capstone-Research-Project
SOAP(Students Organized Against Pollution)

Christopher Smith
SOAP Capstone Project

Here are some python files I've created for my Capstone Research Project.
A description is given for each file listed. An example of front end development with HTML and javascript is found in index.htm. 

## clustering.py

This file uses DBSCAN which is a python library which creates clusters(groupings) out of given data. My code implements this algorithm to create a yellow cluster which is a grouping for potentially contaminated areas and a red cluster which is a different grouping for likely contaminated areas.

Screenshot of output where locations are plotted by their longitude and latitude coordinates. The red circles represent the likely contaminated areas and the yellow circles represent potentially contaminated areas.

![Alt text](relative/path/to/img.jpg?raw=true "clusteringAlgorithm")
##coordinates.py

This file uses the geopy library to convert addresses into a geolocation with x and y coordinates.

## pythonWebscraper.py

Webcrawler that uses selenium to navigate to active contaminated sites on the NJDEP website for Trenton locations. Once it navigates to a specific page, addresses for each site in the Trenton area are stored in a file named addresses.csv.

## index.htm

Html page that can be hosted on localhost that uses the javascript library leaflet which is a mapping tool. Using the longitude and latitude coordinates that were converted with coordinates.py, each brownfield location is displayed using OpenStreetMap. Also, cluster groups are shown using yellow(potentially contaminated) and red(likely contaminated) zones.

To run this file use the command python -m http.server after downloading a stable version of leaflet at 
![Image of Clustering]
(https://github.com/TCNJsmithc69/My-Capstone-Research-Project/edit/main/images/clusteringAlgorithm.png)

Screenshot of output for OpenStreetMap locations.
