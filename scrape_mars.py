# -*- coding: utf-8 -*-
"""
Created on Wed May  1 10:05:26 2019

@author: andre
"""

# Dependencies
from bs4 import BeautifulSoup as bs
import requests
import os
import requests
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
import pandas as pd

def init_browser():
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser()

def scrape():
    mars_data = {}
    mars_data["news_data"] = marsNewsData()
    mars_data["mars_featured_image"] = marsFeaturedImage()
    mars_data["mars_weather"] = marsWeather()
    mars_data["mars_facts_table"] = marsFacts()
    mars_data["mars_hemispheres"] = marsHemisphereImages()
    return mars_data



# Mars News Data
def marsNewsData():
    
# Mars Featured Image
def marsFeaturedImage():
    
# Mars Weather Data
def marsWeather():
    
# Mars Facts
def marsFacts():
    
# Mars Hemisphere Images
def marsHemisphereImages():    
    
