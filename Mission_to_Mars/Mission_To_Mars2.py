from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pymongo
from pymongo import MongoClient
import pandas as pd

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
def Mars_News():
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
    article_date=articles[0]
    article_title=articles[1]
    article_text=articles[2]
    return article_date, article_title ,article_text

def Mars_Images():
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    browser.click_link_by_partial_text('FULL IMAGE')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image_url = soup.find(class_='img')
    if image_url is not None:
        print(image_url)
        url_i=image_url.img['src']
        feautured_image_url = url_i
        print("https://www.jpl.nasa.gov"+feautured_image_url)
        return "https://www.jpl.nasa.gov"+feautured_image_url
    else:
        print("NONETYPE")
        return "Image is not available"

def Mars_Weather():
    html = "https://twitter.com/marswxreport?lang=en"
    browser.visit(html)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    weather = soup.find(class_='js-tweet-text-container')
    mars_weather=weather.p.text
    if mars_weather is not None:
        return mars_weather
    else:
        return "Weather not available"
  

def Mars_Facts():
    mars_facts = pd.read_html('https://space-facts.com/mars/')
    mars_facts=mars_facts[0]
    mars_facts.columns=["Fact", "Value"]
    mars_facts.to_html("Mars_Facts.html",index=False,justify='center')
    mars_facts_table = mars_facts.to_html(index=False, justify='center')
    return mars_facts_table

def Mars_Hemispheres():
    url = "https://www.planetary.org/blogs/guest-blogs/bill-dunford/20140203-the-faces-of-mars.html"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    url2 = soup.find_all(class_='img840')
    hemis=[]
    for image in url2:
        hemis.append(image['src'])
    
    cerberus = hemis[2]
    valles = hemis[0]
    syrtis = hemis[1]
    schiaparelli = hemis[3]

    return cerberus, valles, syrtis, schiaparelli
  

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
        