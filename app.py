# -*- coding: utf-8 -*-
"""
Created on Wed May  1 13:50:01 2019

@author: andre
"""
# Dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


@app.route("/")
def home():

    


@app.route("/scrape")
def scrape():

   

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)