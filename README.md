# WebScraping-Challenge
Its a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

Step 1 - Scraping:
Initial scraping done using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

  NASA Mars News:
    Scrapes the NASA Mars News Site and collects the latest News Title and Paragraph Text. Assigned the text to variables that can be referenced later.
  JPL Mars Space Images - Featured Image:
    Used splinter to navigate the site and find the image url for the current Featured Mars Image and assigned the url string to a variable called featured_image_url.Found the image url to the full size .jpg image.

  Mars Weather:
    Visited the Mars Weather twitter account and scraped the latest Mars weather tweet from the page. Saved the tweet text for the weather report as a variable called mars_weather.

  Mars Facts:
    Visited the Mars Facts webpage and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
Used Pandas to convert the data to a HTML table string.
  
  Mars Hemispheres:
    
