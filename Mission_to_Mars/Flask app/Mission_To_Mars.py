from bs4 import BeautifulSoup;
from splinter import Browser;
import requests
import pymongo
from pymongo import MongoClient
import pandas as pd

def Mars_News():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    articles = []
    for x in range(1, 6):
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.find_all(class_='content_title')
        texts = soup.find_all(class_='article_teaser_body')
        dates = soup.find_all(class_='list_date')
            
        for title,text,date in zip(titles,texts,dates):       
            date = date.text
            title = title.text
            text = text.text
            print("-------------")
            print(f"Article date: {date}")
            print(f"Article title: {title}")
            print(f"Article text: {text}")
            articles.append(date)
            articles.append(title)
            articles.append(text)
    articles[0]
    articles[1]
    articles[2]

def Mars_Images():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    browser.click_link_by_partial_text('FULL IMAGE')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image_url = soup.find(class_='fancybox-inner fancybox-skin fancybox-dark-skin fancybox-dark-skin-open')
    print("IMAGEN!!!! --------------"+image_url)
    url_i=image_url.img['src']
    feautured_image_url = url_i
    print("https://www.jpl.nasa.gov"+feautured_image_url)

def Mars_Weather():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    html = "https://twitter.com/marswxreport?lang=en"
    browser.visit(html)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    weather = soup.find(class_='js-tweet-text-container')
    mars_weather=weather.p.text
    mars_weather

def Mars_Facts():
    mars_facts = pd.read_html('https://space-facts.com/mars/')[0]
    mars_facts
    mars_facts.columns=["Fact", "Value"]
    mars_facts.set_index("Fact", inplace=True)
    mars_fact = mars_facts.to_html("Mars_Facts.html",index=False)
    mars_facts

def Mars_Hemispheres():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    hemispheres=["Cerberus Hemisphere Enhanced", "Schiaparelli Hemisphere Enhanced","Syrtis Major Hemisphere Enhanced","Valles Marineris Hemisphere Enhanced"]
    arreglo=[]
    for hemi in hemispheres:
        browser.visit(url)
        browser.click_link_by_partial_text(hemi)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        url2 = soup.find(class_='wide-image')
        img_url2=url2['src']
        print(f"https://astrogeology.usgs.gov{img_url2}")
        hemi_url=("https://astrogeology.usgs.gov"+img_url2)
        arreglo.append(hemi_url)
    arreglo

# def mongodb():
#     conn="mongodb://localhost:27017"
#     client = pymongo.MongoClient(conn)
#     db = client.mission_to_mars
#     db.mission_to_mars.insert_many([
#         {
#             "articles":articles,
#             "feautured_image_url":feautured_image_url,
#             "mars_weather":mars_weather,
#             "mars_hemispheres":arreglo,
#             "mars_facts":mars_fact
#         }])
        