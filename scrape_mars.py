# -*- coding: utf-8 -*-
"""
Created on Wed May  1 10:05:26 2019

@author: andre
"""

# Dependencies
from bs4 import BeautifulSoup as bs
import requests
import os
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
import pandas as pd
import time



#Setup splinter browser
def init_browser():
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)



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
    browser = init_browser()    
    mars_images_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(mars_images_url)
    time.sleep(5)
    
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    
    featured_image_url = browser.find_by_css('.fancybox-image').first['src']
    time.sleep(5)
    
    return featured_image_url

    
    
# Scrape Mars Weather Data
def marsWeather():
    twitter_url = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(twitter_url)
    time.sleep(5)

    soup2 = bs(response.text, 'html.parser')
    time.sleep(5)
    
    mars_weather = []
    for weather in soup2.find_all('p',class_ = "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"):
        mars_weather.append(weather.text.strip())

    weather_tweet = mars_weather[0]

    return weather_tweet


    
# Scrape Mars Facts
def marsFacts():
    mars_facts_url = 'https://space-facts.com/mars/'
       
    mars_facts = pd.read_html(mars_facts_url)
    time.sleep(5)
    
    mars_facts_df = mars_facts[0]
    mars_facts_df.columns = ['Fact Type', 'Data']
    
    mars_facts_html = mars_facts_df.to_html(header=True, index=False)
    
    return mars_facts_html


    
# Scrape Mars Hemisphere Images
def marsHemisphereImages():    
    browser = init_browser()
    usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(usgs_url)
    time.sleep(5)
        
    label1 = browser.find_by_tag('h3')[0].text
    label2 = browser.find_by_tag('h3')[1].text
    label3 = browser.find_by_tag('h3')[2].text
    label4 = browser.find_by_tag('h3')[3].text
    time.sleep(5)

    browser.find_by_css('.thumb')[0].click()
    image1 = browser.find_by_text('Sample')['href']
    browser.back()
    time.sleep(5)

    browser.find_by_css('.thumb')[1].click()
    image2 = browser.find_by_text('Sample')['href']
    browser.back()
    time.sleep(5)

    browser.find_by_css('.thumb')[2].click()
    image3 = browser.find_by_text('Sample')['href']
    browser.back()
    time.sleep(5)

    browser.find_by_css('.thumb')[3].click()
    image4 = browser.find_by_text('Sample')['href']
    browser.back()
    time.sleep(5)

    mars_hem_images=[{'title':label1, 'image_link': image1},
                   {'title':label2,'image_link': image2},
                   {'title':label3, 'image_link': image3},
                   {'title':label4,'image_link':image4}]

    return mars_hem_images

    browser.quit()

   
    
   
    
    
    
