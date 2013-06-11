from BeautifulSoup import BeautifulSoup, SoupStrainer
import re
import urllib2

website = input('Enter full website domain as quoted string: ')

#Return list of clean string urls from given clean string website url
def getLinks(website):
    hierarchy = [website]
    linklist = []
    links =  BeautifulSoup(urllib2.urlopen(website)).findAll('a')
    for l in links:
        """
        #Filter link results to only specific things
        if 'specific' in l['href']:
            linklist.append(l)
        """
        linklist.append(l['href'])
    #Clean up the results 
    for item in linklist:
        #Clean up the results to only external webpages
        if '.' in str(item):
            hierarchy.append(str(item))
    print hierarchy
    return hierarchy

#Recursively go through list and generate hierarchy of urls as lists
def getLinksOfLinks(webList):
    for sub1 in range(len(webList)):
        if type(webList[sub1]) == list:
            webList[sub1] = getLinksOfLinks(webList[sub1])
        elif type(webList[sub1]) == str:
            print "Hit a url"
            if website in webList[sub1]:
                if website == webList[sub1]:
                    continue
                print "In an intenal link. Following... " + webList[sub1]
                webList[sub1] = [webList[sub1]]
                webList[sub1].extend(getLinks(webList[sub1][0]))
        else:
            print "Error: Parse Error"
        print "**** UPDATED WEB LIST  ****"
        prettyprint(webList)
        print "**** END UPDATED ****"
    return webList

#Helper
def listify(linklist):
    if type(linklist) == list:
        for x in range(len(linklist)):
            linklist[x] = [linklist[x]]
    elif type(linklist) == str:
        return [linklist]
    else:
        print "Error: Parse Listify Error"

def prettyprint(siteMap, order = 0):
    level = order
    for i in range(len(siteMap)):
        if type(siteMap[i]) == str:
            print "-" * (level + 1) + "> " + siteMap[i]
        elif type(siteMap[i]) == list:
            prettyprint(siteMap[i], level + 1 )
            

#Process
print getLinksOfLinks(getLinks(website))

