# NewsScraper 
# A Python Script that scrapes the web for Headlines and reads them out loud
# Author: Aayush Dawra


#Dependencies installed and ready
import os
from bs4 import BeautifulSoup
import mechanize

url = "http://www.nytimes.com/"

#Fetches basic HTML and spits that out
def fetchHTML(url):
	br = mechanize.Browser()
	html = br.open(url)
	return html.read()

#Use os.system("...") ti run a command line argument
