from BeautifulSoup import BeautifulSoup, SoupStrainer
import re
import urllib2

website = input('Enter full website domain as quoted string: ')
#List representation of SiteMap
hierarchy = [[website]]
linklist = []

def getLinks(website):
    links =  BeautifulSoup(urllib2.urlopen(website)).findAll('a')
    for l in links:
        """
        #Filter link results to only specific things
        if 'specific' in l['href']:
            linklist.append(l)
        """
        linklist.append(l['href'])

getLinks(website)
for item in linklist:
    #print item
    #Clean up the results to only external webpages
    if '.' in item:
        hierarchy.append(str(item))
        print item
print hierarchy
#For testing
links = BeautifulSoup(urllib2.urlopen(website))
