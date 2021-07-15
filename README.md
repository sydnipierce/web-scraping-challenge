# web-scraping-challenge
HW 12

This project uses BeautifulSoup and Splinter to scrape several websites with data on the Mars mission, pass the data collected into MongoDB, and use Flask to query MongoDB and render the data on a webpage.

## File Organization

The main Missions_to_Mars folder contains:

* mission_to_mars.ipynb: A Jupyter notebook file where the scraping script is located.
* mission_to_mars.py: The converted version of the Jupyter notebook file pulling all scraping code into a Python function.
* webpage_screenshot.png: A screenshot of the final web page.

### Sub-Folders

* templates: Contains the index.html file used to render the web page.
* static/stylesheets: Contains the CSS file.
