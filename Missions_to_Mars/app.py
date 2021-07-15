from flask import Flask, render_template, redirect
import pymongo
from mission_to_mars import scrape

app = Flask(__name__)

# Use pymongo to set up mongo connection
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.mars

db.latest_data.drop()

db.latest_data.insert(scrape())

@app.route('/')
def index():
    data = list(db.latest_data.find())
    print(data)

    news_title = data["Latest News"]["Titles"][0]
    news_blurb = data["Latest News"]["Blurbs"][0]

    feat_image = data["Featured Image"]

    facts_table = data["Facts"]

    hemi_images = data["Hemisphere Images"]

    return render_template('index.html', )


@app.route('/scrape')
def scraper():
    mars = mongo.db.mars
    mars_data = mission_to_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)