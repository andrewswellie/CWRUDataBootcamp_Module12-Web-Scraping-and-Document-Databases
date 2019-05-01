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

#Setup splinter browser
def init_browser():
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=True)

#Create the scrape function that will run all the other functions and return the outputs
def scrape():
    mars_data = {}
    mars_data["news_data"] = marsNewsData()
    mars_data["mars_featured_image"] = marsFeaturedImage()
    mars_data["mars_weather"] = marsWeather()
    mars_data["mars_facts_table"] = marsFacts()
    mars_data["mars_hemispheres"] = marsHemisphereImages()
    return mars_data


# Scrape Mars News Data
def marsNewsData():
    news_data = {}

    mars_articles_url = 'https://mars.nasa.gov/news/'
    response = requests.get(mars_articles_url)
    time.sleep(5)

    soup = bs(response.text, 'html.parser')
    time.sleep(5)
    news_title=soup.find(class_="content_title").text.strip('\n')
    news_p=soup.find(class_="rollover_description_inner").text.strip('\n')

    news_data["news_title"]= news_title
    news_data["paragraph_text"]= news_p

    return news_data
    
# Scrape Mars Featured Image
def marsFeaturedImage():
    browser = initBrowser()    
    mars_images_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(mars_images_url)
    time.sleep(5)
    
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    
    featured_image_url = browser.find_by_css('.fancybox-image').first['src']
    time.sleep(5)
    
    browser.quit()

    return featured_image_url
    
# Scrape Mars Weather Data
def marsWeather():
    twitter_url = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(twitter_url)
    time.sleep(5)

    soup = bs(response.text, 'html.parser')
    time.sleep(5)
    
    mars_weather = []
    for weather in soup.find_all('p',class_ = "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"):
        mars_weather.append(weather.text.strip())

    weather_tweet = mars_weather[0]

    return weather_tweet
    
# Scrape Mars Facts
def marsFacts():
    
# Scrape Mars Hemisphere Images
def marsHemisphereImages():    
    
