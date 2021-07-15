from flask import Flask, render_template, redirect
import pymongo
from mission_to_mars import scrape

app = Flask(__name__)

# Use pymongo to set up mongo connection
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.mars

@app.route('/scrape')
def scraper():
    db.latest_data.drop()

    db.latest_data.insert_one(scrape())

    return redirect("/", code=302)

@app.route('/')
def index():
    data = list(db.latest_data.find())
    print(data)
    news_title = data[0]['Latest News'][0]['Titles'][0]
    
    news_blurb = data[0]['Latest News'][1]['Blurbs'][0]

    feat_image = data[0]["Featured Image"]

    facts_table = data[0]["Facts"]

    hemi_images = data[0]["Hemisphere Images"][0]

    return render_template('index.html', news_title=news_title, news_blurb=news_blurb, feat_image=feat_image, facts_table=facts_table)

if __name__ == "__main__":
    app.run(debug=True)