from BeautifulSoup import BeautifulSoup
import re
import urllib2

website = input('Enter full website domain as quoted string: ')
#List representation of SiteMap
hierarchy = [[website]]
linklist = []

def getLinks(website):
    links =  BeautifulSoup(urlliab2.urlopen(website)).findAll('a')
    for l in links:
        linklist.append(l)

getLinks(website)
for item in linklist:
    print item
    if "href" in item:
        print item

print getLinks
