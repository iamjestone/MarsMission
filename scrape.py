from bs4 import BeautifulSoup 
from splinter import Browser
import pandas as pd 
import requests 

def init_browser():

    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

marsstuff = {}

def marsscrape1():
    try:  # Initialize browser 
        browser = init_browser()

        url = 'https://mars.nasa.gov/news/'
        browser.visit(url)

        html = browser.html

        soup = BeautifulSoup(html, 'html.parser')


        # Retrieve the latest element that contains news title and news_paragraph
        newstitle = soup.find('div', class_='content_title').find('a').text
        newswords = soup.find('div', class_='article_teaser_body').text

        marsstuff['newstitle'] = newstitle
        marsstuff['newswords'] = newswords

        return marsstuff
    finally:
        browser.quit()
