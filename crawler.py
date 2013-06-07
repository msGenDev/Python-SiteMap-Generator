from BeautifulSoup import BeautifulSoup
import re
import urllib2

website = input('Enter full website domain as quoted string: ')
links =  BeautifulSoup(urllib2.urlopen(website)).findAll('a')
for l in links:
    print l
