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


