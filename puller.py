#Web scraper and sorter
#For personal, non-profit use

from requests import get

def input(s):
    str(s)
    r = get(s)
    print r.text
    return 

site = raw_input("What site are we scraping? ")

print "Retrieving data for %s" % site

input(site)


