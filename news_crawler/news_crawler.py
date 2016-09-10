import mechanize
import urllib
from bs4 import BeautifulSoup
def getHtmlText(url):
        a = ""
	br = mechanize.Browser()    #create an browser opener object. 
	br.set_handle_robots(False)
	br.addheaders = [('User-agent','Mozilla')]
	htmltext = br.open(url).read()     # htmltext use opener object to open a file and read it. 
	soup = BeautifulSoup(htmltext)
        for tag in soup.findAll('p', attrs = {"class": "p-block"}):
            a += tag.contents[0] + '\n' + '\n'
	    
	print a
	
	 
def getHtmlFile(url):
	br = mechanize.Browser()
	htmlfile= br.open(url)
	return htmlfile

	
			
getHtmlText("http://www.nytimes.com/aponline/2016/05/03/world/europe/ap-soc-champion-leicester.html?ref=world")

###BeutifulSoup receives br.open() or br.open().read()
###maximum recursion exceeded when calling an object, use too many loops or recursions. assign them to one variable  

###basic idea: use mechanize to get the html and BeautifulSoup to get the elements and print them out. get nytime.com's article. 