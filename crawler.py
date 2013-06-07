from BeautifulSoup import BeautifulSoup
import re
import urllib2

page = urllib2.urlopen("http://example.com")
soup = BeautifulSoup(page)
links = soup.findAll('a')
for l in links:
    print l
