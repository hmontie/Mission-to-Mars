# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import dateime as df

def scrap_all():
    #Set the executable path and initialize the chrome browser in splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)
    
     # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "hemisphere": hemispheres(browser),
        "last_modified": dt.datetime.now()
    }
    
     # Stop webdriver and return data
    browser.quit()
    return data


def mars_news(browser):
    
    # Scrape Mars News
    # Visit the mars nasa news site
    url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
    browser.visit(url)
   
    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    #Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')
   
    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')
        slide_elem.find('div', class_='content_title')
        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
            return None, None
        
    return news_title,news_p

# ### JPL Space Images Featured Image

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit URL
def featured_image(browser):
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')
    
    # Add try/except for error handling
    try:
    # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
    
    except AttributeError:
        return None
    
    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return img_url
# ### Mars Facts


def mars_facts():
    #Add try/except for error handling
    try:
       # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    except BaseException:
        return None
        
        #Assign columns and set index of df
        df.columns=['description', 'Mars', 'Earth']
        df.set_index('description', inplace=True)
        df

        # Convert dataframe into HTML add bootstrap
        return df.to_html()
if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all()) 

# Challenge
def hemispheres(browser):
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    hemisphere_image_urls = []

    # First get the list of all hemisphers
    links = browser.find_by_css('a.product-item h3')

    # Next loop through those links click the link find the sample anchor return href
    for index in range(len(links)):

    # We have to find the elements on each loop to avoid a state element exception
    browser.find_by_css('a.product-item h3')[index].click()
    hemisphere_data = scrape_hemisphere(browser.html)
    
    hemisphere_image_urls.append(hemisphere_data)
    
    # Finally we navigate backwards
    browser.back()
    return hemisphere_image_urls

def scrape_hemisphere(html_text):
    # parse html text
    hemi_soup = soup(html_text, "html.parser")

    try:
        title_element = hemi_soup.fiond("h2", class_="title").get_text() 
        sample_element = hemi_soup.find("a", text="Sample").get("href")
    except AttributeError:
        tittle_element = None
        sample_element = None
    hemispheres_dictionary = {
        "title": title_element,
        "img_url": sample_element
    }
    return hemispheres_dictionary

if __name__ == "__main__":
    print(scrape_all())