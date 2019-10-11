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

   ![Featured Mars Image](Instructions/Images/final_app_part1.png)

   
  Mars Hemispheres:
   Visited the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres.

   Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Used a Python dictionary to store the data using the keys img_url and title.

   Appended the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere. 
   ![Featured Mars Image](Instructions/Images/final_app_part2.png)

Step 2 - MongoDB and Flask Application:

Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

Converted the Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of the scraping code from above and return one Python dictionary containing all of the scraped data.

Next, created a route called /scrape that will import scrape_mars.py script and calls the scrape function.

Stored the return value in Mongo as a Python dictionary.
Created a root route / that will query the Mongo database and pass the mars data into an HTML template to display the data.

Created a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements.

A screenshot of the index.html page

![Featured Mars Image](Instructions/Images/screencapture.png)
