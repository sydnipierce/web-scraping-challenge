from flask import Flask, render_template, redirect
import pymongo
from mission_to_mars import scraping_results

app = Flask(__name__)

# Use pymongo to set up mongo connection
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.mars

db.latest_data.drop()

db.latest_data.insert(scraping_results)

@app.route("/")
def index():
#    listings = mongo.db.listings.find_one()
    return render_template("index.html")


@app.route("/scrape")
def scraper():
    mars = mongo.db.mars
    mars_data = mission_to_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)