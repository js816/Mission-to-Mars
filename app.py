# Importing the dependencies
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

# Setting up Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Adding the index route
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()  # finds the mars collection within the database
    return render_template("index.html", mars=mars) # uses the index.html file we'll create, mars=mars uses the mars collection in db

# Adding the scrape route
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars # variable to point to mars db
    mars_data = scraping.scrape_all() # variable to hold scraped data, referencing scrap_all function in the scraping.py file
    mars.update({}, mars_data, upsert=True) # updating the database with mars_data (query_parameter, data, options), upsert creates new document if one doesn't already exist
    return redirect('/', code=302) # after scraping will return to / and we'll see updated data

if __name__ == "__main__":
    app.run()