from bs4 import BeautifulSoup
def getArticleText(webtext):
	soup = BeautifulSoup(webtext)
	print soup
	for tag in soup.findAll('p', attrs = {"class": "story-body-text"}):
		print tag
