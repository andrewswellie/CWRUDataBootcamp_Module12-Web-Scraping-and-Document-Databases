# -*- coding: utf-8 -*-
"""
Created on Wed May  1 13:50:01 2019

@author: andre
"""
# Dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pymongo



# create instance of Flask app
app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.scrape_mars
collection = db.data

# Route to render index.html template and find mongo documents
@app.route("/")
def index():
    mars_final_data = db.collection.find_one()

    # Return template and data
    return render_template("index.html", mars=mars_final_data)



# Route that will trigger scrape functions
@app.route("/scrape")
def scrape():
   
   # Run the scrape function
    mars_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")
    

if __name__ == "__main__":
    app.run(debug=True)