# -*- coding: utf-8 -*-
"""
Created on Wed May  1 13:50:01 2019

@author: andre
"""
# Dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)


@app.route("/")
def home():
    # Find one record of data from the mongo database
    #destination_data = mongo.db.collection.find_one()

    # Return template and data
    #return render_template("index.html", vacation=destination_data)    


@app.route("/scrape")
def scrape():
    # Run the scrape function
    #costa_data = scrape_costa.scrape_info()

    # Update the Mongo database using update and upsert=True
    #mongo.db.collection.update({}, costa_data, upsert=True)

    # Redirect back to home page
    return redirect("/")

   

       
if __name__ == "__main__":
    app.run(debug=True)