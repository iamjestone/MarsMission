from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import pymongo

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()
    newsinfo = {}

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    newsinfo["title"] = soup.find("a", target_="self").get_text()
    newsinfo["text"] = soup.find("div", class_="article_teaser_body").get_text()

    return newsinfo