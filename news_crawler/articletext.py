from bs4 import BeautifulSoup
def getArticleText(webtext):
	soup = BeautifulSoup(webtext)
	#print soup
	for tag in soup.findAll('div', attrs = {"id": "mw-content-text"}):
		print (tag)
getArticleText("https://en.wikipedia.org/wiki/Gangu_Teli")