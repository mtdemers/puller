#Web scraper and sorter
#For personal, non-profit use
from bs4 import BeautifulSoup #HTML parsing
from requests import get #HTML requests

def scrape(s):
    str(s) #change site to string
    r = get(s) #scrape site data
    data = r.text #change site data to text
    soup = BeautifulSoup(data, "html.parser")  #parse text
    print soup #display parsed text


site = raw_input("What site are we scraping? ") #input site

print "Retrieving data for %s" % site

scrape(site) #pass site to scrape
