'''
Christopher Smith

Webscraper and webcrawler that navigates to the NJDEP active sites in Mercer County using Selenium 
then extracts all addresses that are located within the Trenton Area. Stores all address information
into a csv file labeled addresses.csv located within the data folder.

'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

def webCrawler(driver):
    #navigate to NJDEP known contaminated sites website
    driver.get("https://www.state.nj.us/dep/srp/kcsnj/")
    #click on active sites link
    element = driver.find_element_by_xpath("//ul[(((count(preceding-sibling::*) + 1) = 4) and parent::*)]//a")
    element.click()
    #select mercer from the drop down menu
    select = Select(driver.find_element_by_name('Select 1 or more Counties:'))
    select.select_by_value('Mercer;')
    #uncheck the checkmark that says view report by pages
    checkmark = driver.find_element_by_xpath("//*[(@id = 'ShowInPages')]")
    checkmark.click()
    #click submit
    submit = driver.find_element_by_id("btnRunReport")
    submit.click()
    #give ten seconds for the page to load
    time.sleep(10)

def webScraper(driver):
    data = []
    sitelist = []
    #collect all sites that are within the Trenton area
    sites = driver.find_elements_by_css_selector("tr:nth-child(11) .bc .s9:nth-child(3) .vai")
    #collect all addresses for each site within the Trenton area
    addresses = driver.find_elements_by_css_selector("tr:nth-child(11) .bc .s9:nth-child(4) .vai")

    #convert each site that is collected into text
    for site in sites:
        site_text = site.text
        sitelist.append(site_text)

    #convert each address that is collected into text
    for address in addresses:
        address_text = address.text
        #append Trenton New Jersey at the end of the address
        address_text = address_text + " Trenton New Jersey"
        data.append(address_text + " Trenton New Jersey")

    #create a dataframe with columns Site and Address   
    d = {'Site': sitelist, 'Address': data}
    data_addresses = pd.DataFrame(d)
    #store dataframe into a csv file
    data_addresses.to_csv('data/addresses.csv', index=False)

#change this path to where your chromedriver executable is located
driver = webdriver.Chrome(executable_path='C:/Users/Chris-Pc/Desktop/SOAP Research Project/chromedriver.exe')
webCrawler(driver)
webScraper(driver)
driver.quit()

