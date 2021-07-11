#!/usr/bin/env python
# coding: utf-8

# In[1]:

def scrape():

    # Import dependencies
    import os
    from bs4 import BeautifulSoup as bs
    import pandas as pd
    import requests
    from splinter import Browser
    from webdriver_manager.chrome import ChromeDriverManager


    # ## NASA Mars News

    # In[2]:


    # Set URL to scrape
    url = "https://redplanetscience.com/"

    # Use requests to pull site content
    response = requests.get(url)


    # In[3]:


    # Create a BeautifulSoup object and parse
    soup = bs(response.text, 'html.parser')

    # Print site's HTML content
    print(soup.prettify())


    # In[4]:


    # HTML not displaying article content
    # Initiate browser driver to click search button, then pull HTML
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[5]:


    # Visit site
    browser.visit(url)


    # In[6]:


    # Find and click the 'search' button
    search_button = browser.find_by_css('.search_submit')
    search_button.click()


    # In[7]:


    # Pull HTML content
    html = browser.html
    soup = bs(html, 'html.parser')

    print(soup.prettify())


    # In[8]:


    # Pull article titles from HTML
    titles = soup.find_all('div', class_='content_title')
    titles


    # In[9]:


    # Create a list to hold title text
    title_list = []

    # Assign titles to list
    for title in titles:
        title_list.append(title.text)
        
    title_list


    # In[10]:


    # Pull preview paragraphs from HTML
    paragraphs = soup.find_all('div', class_='article_teaser_body')
    paragraphs


    # In[11]:


    # Create a list to hold description text
    descrip_list = []

    # Assign titles to list
    for blurb in paragraphs:
        descrip_list.append(blurb.text)
        
    descrip_list


    # ## JPL Mars Space Images

    # In[12]:


    # Establish second URL
    url = "https://spaceimages-mars.com/"

    # Visit site
    browser.visit(url)


    # In[13]:


    # Pull HTML content
    html = browser.html
    soup = bs(html, 'html.parser')

    print(soup.prettify())


    # In[14]:


    # Locate link associated with full header image
    header_image = browser.links.find_by_partial_text('FULL IMAGE')

    # Pull href from this element and save in variable
    featured_image_url = header_image['href']
    featured_image_url


    # ## Mars Facts

    # In[15]:


    # Establish third URL
    url = "https://galaxyfacts-mars.com/"


    # In[16]:


    # Scrape tables on page
    tables = pd.read_html(url)
    tables


    # In[17]:


    # Pull desired table
    planet_facts = tables[0]
    planet_facts


    # In[18]:


    # Drop Earth from table
    mars_facts = planet_facts.iloc[:, 0:2]
    mars_facts


    # In[19]:


    # Fix header
    # Pull header row
    header_row = mars_facts.iloc[0]

    # Pull rest of table minus header row
    clean_facts_df = mars_facts.iloc[1:7,:]

    # Put correct header on table
    clean_facts_df.columns = header_row

    clean_facts_df


    # In[20]:


    # Convert df to HTML
    facts_table_html = clean_facts_df.to_html()
    facts_table_html


    # ## Mars Hemispheres

    # In[21]:


    # Establish fourth URL
    url = "https://marshemispheres.com/"

    # Visit site
    browser.visit(url)


    # In[22]:


    # Pull HTML content
    html = browser.html
    soup = bs(html, 'html.parser')

    print(soup.prettify())


    # In[23]:


    # Locate link associated with full header image
    hemi_links = browser.links.find_by_partial_text('Enhanced')

    hemi_list = []

    for link in hemi_links:
        hemi_dict = {"title": "", "img_url": ""}
        hemi_dict["img_url"] = link['href']
        hemi_dict["title"] = link.text
        hemi_list.append(hemi_dict)

    for record in hemi_list:
        url = record["img_url"]
        browser.visit(url)
        img = browser.links.find_by_partial_text('Sample')
        img_link = img['href']
        record["img_url"] = img_link

    hemi_list


    # In[24]:


    ## Verify 4 links were found
    # for item in hemi_links:
    #     hemi_list.append(item)
        
    # hemi_list


    # In[ ]:

    scraping_results = {
        "Latest News": [
            {"Titles": title_list},
            {"Blurbs": descrip_list}
        ],
        "Featured Image": featured_image_url,
        "Facts": facts_table_html,
        "Hemisphere Images": hemi_list
    }

    return(scraping_results)


