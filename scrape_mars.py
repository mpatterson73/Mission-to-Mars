#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from selenium import webdriver
import lxml
import os
from time import sleep


# In[2]:



# In[3]:


# Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) 
# and collect the latest News Title and Paragraph Text. 

url = 'https://mars.nasa.gov/news/'
driver = webdriver.Chrome()
driver.get(url)
# Create BeautifulSoup object
soup = bs(driver.page_source, 'html.parser')


# In[4]:


news_title = soup.find('div', class_='content_title').text
print(f"Most Recent Title: {news_title}")
news_p = soup.find('div', class_='article_teaser_body').text
print(f"First Paragraph: {news_p}")
driver.close()


# In[5]:


# Use splinter to navigate the site and find the image url for the current Featured Mars Image and 
# assign the url string to a variable called `featured_image_url`.


# In[6]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
html = browser.html
soup = bs(html, 'html.parser')


# In[7]:


# Navigate to the page with the full, large image
browser.click_link_by_id('full_image')
sleep(5)
browser.click_link_by_partial_text('more info')


# In[8]:


html = browser.html
soup = bs(html, 'html.parser')
image_url = soup.find('img').get('src')
base_url = "https://www.jpl.nasa.gov/spaceimages"
featured_img_url = base_url + image_url
print (f"The featured image's URL is: {featured_img_url}")


# In[9]:


### Mars Weather
# Visit the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) 
# Scrape the latest Mars weather tweet from the page. 
# Save the tweet text for the weather report as a variable called `mars_weather`.


# In[10]:


twitter_wx_url = "https://twitter.com/marswxreport?lang=en"
tweet_response = requests.get(twitter_wx_url)
tweet_soup = bs(tweet_response.text, 'html.parser')
mars_weather = tweet_soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
print("Today's weather on Mars:")
print(mars_weather)


# In[11]:


### Mars Facts

# Visit the Mars Facts webpage [here](http://space-facts.com/mars/) 
# Use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

mars_facts_url = "http://space-facts.com/mars/"
sleep(3)  
mars_table = pd.read_html(mars_facts_url) 
mars_facts_df = mars_table[0]
mars_facts_df


# In[12]:


# Use Pandas to convert the data to a HTML table string.
html_table = mars_facts_df.to_html()
print(html_table.translate({ord('\n'): None}))


# In[13]:


### Mars Hemispheres

# Visit the USGS Astrogeology site [here]:
# (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) 
# to obtain high resolution images for each of Mar's hemispheres.


# In[14]:


base_url = "https://astrogeology.usgs.gov/"
hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hemi_url)
hemi_html = browser.html
hemi_soup = bs(hemi_html, 'html.parser')


# In[15]:


# Use a Python dictionary to store the data using the keys `img_url` and `title`.
# Append the dictionary with the image url string and the hemisphere title to a list. 
# This list will contain one dictionary for each hemisphere.


# In[16]:


hemi_dict_list = []
items = hemi_soup.findAll('div', class_='item')
# Save both the image url string for the full resolution hemisphere image, 
# and the Hemisphere title containing the hemisphere name. 
for item in items:
    title = item.find('h3').text
    # Click each of the links to the hemispheres in order to find the image url to the full resolution image.
    browser.click_link_by_partial_text('Hemisphere Enhanced')
    browser.windows.current
    hemi_img_soup = bs(browser.html, 'html.parser')
    hemi_img_full = hemi_img_soup.find('div', class_='downloads')
    hemi_img_url = hemi_img_full.find('a').get('href')
    hemi_dict = {'title':title , 'image url': hemi_img_url}
    hemi_dict_list.append(hemi_dict)
browser.quit()
hemi_dict_list  


# In[ ]:





# In[ ]:



