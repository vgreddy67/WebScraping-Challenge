# Dependencies
import requests
from bs4 import BeautifulSoup
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
import pandas as pd

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    
    browser = init_browser()
    
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    
    # Create BeautifulSoup object; parse with 'lxml'
    html = browser.html
    soup = BeautifulSoup(html, 'lxml')

    # Retreiving the unordered list with its class name(as latest news are present in an unordered list)
    unorder_lst = soup.find('ul', class_='item_list')

    # Retreiving the first list item (as this will be the latest news)
    news_lst = unorder_lst.find('li')

    #Retreiving the latest news title
    title = news_lst.find('div',class_='content_title')

    #Storing the latest news title in a variable(after stripping all the extra data)
    news_title = title.text.strip()

    #Retreiving & Storing the latest news teaser in a variable(after stripping all the extra data)
    teaser = news_lst.find('div',class_='article_teaser_body')
    news_p = teaser.text.strip()
    
    #JPL site
    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)

    #Scrape JPL into soup
    html = browser.html
    soup = BeautifulSoup(html,'lxml')

    featured_image = soup.find('div',class_='carousel_container')

    featured_image_title = featured_image.find('footer')
    
    full_img = featured_image_title.find('a')['data-link']

    full_img_url = 'https://www.jpl.nasa.gov' + full_img
    
    #Visiting the page that has the full image details
    browser.visit(full_img_url)
    
    #Scrape full image page to soup
    html = browser.html
    soup = BeautifulSoup(html,'lxml')

    large_img = soup.find('figure',class_='lede')

    #Large image partial url
    large_img_url = large_img.find('a')['href']
   
    #Large image url
    featured_image_url = 'https://www.jpl.nasa.gov' + large_img_url
    
    #Mars Weather on Twitter
    mars_twitter_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(mars_twitter_url)

    html = browser.html
    soup = BeautifulSoup(html,'lxml')

    #Retreiving p tag with specified class name
    stream_items = soup.find('p',class_='tweet-text')

    #Retreiving the text of p tag which is the first element in contents (2nd being the <a> tag i.e child tag of p)
    mars_weather = stream_items.contents[0]
    
    #Removing the newline (\n) character from the retreived text.
    mars_weather = mars_weather.replace('\n',' ')
    
    #Mars facts webpage
    mars_facts_url = 'https://space-facts.com/mars/'

    mars_facts_table = pd.read_html(mars_facts_url)
#     mars_facts_table
    #Fetching Mars Facts table
    mars_facts_df = mars_facts_table[1]
    mars_facts_df.columns = ['Facts','Values']
#     mars_facts_df

    html_table = mars_facts_df.to_html()
    
    new_html_table = html_table.replace('\n','')
    
    #Mars Hemispheres (using class description and h3 text)
    mars_hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars' 

    browser.visit(mars_hemispheres_url)

    html = browser.html
    soup = BeautifulSoup(html,'lxml')

    mars_hemispheres = soup.find_all('div',class_='description')

    hemispheres_text = []
    hemisphere_url_list = []

    #Iterate through the div tags
    for hemisphere in mars_hemispheres:
        #Error handling
        try:
            hemi_url = hemisphere.find('h3')
            hems = hemi_url.text.strip()
            hemispheres_text.append(hems)

            browser.click_link_by_partial_text(hems)

            html = browser.html
            soup = BeautifulSoup(html,'lxml')

            hemis_image = soup.find('div',id="wide-image")
            hemis_image_url = hemis_image.find('img',class_='wide-image')['src']

            hemisphere_url_list.append('https://astrogeology.usgs.gov'+ hemis_image_url)

        except Exception as e:
            a_href_val = hemisphere.find('a')['href']

            miss_url = 'https://astrogeology.usgs.gov'+ a_href_val

            browser.visit(miss_url)

            html = browser.html
            soup = BeautifulSoup(html,'lxml')

            hemis_image = soup.find('div',id="wide-image")
            hemis_image_url = hemis_image.find('img',class_='wide-image')['src']

            hemisphere_url_list.append('https://astrogeology.usgs.gov'+ hemis_image_url)
            
     #Adding the texts and links to a dictionary
    hemisphere_image_urls = []

    for hemi in range(len(hemispheres_text)):
        hem_dict = {
            "title":hemispheres_text[hemi],
            "img_url":hemisphere_url_list[hemi]
        }
        hemisphere_image_urls.append(hem_dict)
        
    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_img_url": featured_image_url,
        "mars_weather": mars_weather,
        "mars_facts": new_html_table,
        "hemispheres_images": hemisphere_image_urls
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data