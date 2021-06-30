#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


# Setting up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the URL to scrape
url = 'https://redplanetscience.com/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


# Parse the HTML
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[5]:


# Capturing the title of the newest article
slide_elem.find('div', class_='content_title')


# In[6]:


# Use the parent element to find the first 'a' tag and save it as 'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the first summary and save it as news_p
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Image

# In[8]:


# Visit the URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


# Parsing the HTML
html = browser.html
img_soup = soup(html, 'html.parser')


# In[11]:


# Finding the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[13]:


# Visit the URL
url = 'https://galaxyfacts-mars.com/'
browser.visit(url)


# In[14]:


# Pull the first table found at the URL and turn it into a DataFrame
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[15]:


# Looking at the second table and turning it into a DataFrame
df2 = pd.read_html('https://galaxyfacts-mars.com')[1] #read_html searches for HTML tables, can add index # if more than one
df2.columns=['description', "Mars"]
df2.set_index('description', inplace=True)
df2


# In[16]:


# Turning the first table back into HTML code
df.to_html()


# In[17]:


# Quitting the browser
browser.quit()

