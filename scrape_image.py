#Zhao Weng web image scraping
#reference 
#getting page source with python
#http://youtube.com/creeveshft
#http://christopherreevesofficial.com
#http://twitter.com/cjreeves2011

import urllib     #get contents, connection, save
import mechanize      #set_handle_robots 
from bs4 import BeautifulSoup     #return python objects 
from urlparse import urlparse
import hashlib                  #hash the image name 

def searchPic(term):
    img_list = getPic(term)
    if len(img_list)>0:
        for img in img_list:
            savePic(img)
            print ("hello")
    print "no"
    print "done..."     

def getPic (search):
    search = search.replace(" ","%20")
    try:
        browser = mechanize.Browser()
        browser.set_handle_robots(False)
        browser.addheaders = [('User-agent','Mozilla')]

        htmltext = browser.open("https://www.google.com/search?site=imghp&tbm=isch&source=hp&biw=1414&bih=709&q="+search+"&oq="+search)
        img_urls = []
        formatted_images = []
        soup = BeautifulSoup(htmltext)
        results = soup.findAll("img")
        
        for r in results:
            try:
                if "encrypted" in r['src']:
                    img_urls.append(r['src'])
                    
            except:
                pass
        print img_urls
        return img_urls
        
        



        #for im in img_urls:
        #    refer_url = urlparse(str(im))
        #    image_f = refer_url.query.split("&")[0].replace("imgurl=","")
        #    formatted_images.append(image_f)
        #
        #return  formatted_images

    except:
        return []
        


def savePic(url):
    hs = hashlib.sha224(url).hexdigest()
    #file_extension = url.split(".")[-1]
    file_extension = "jpg"
    uri = "Desktop/web"      ##nothing means zweng4
    dest = uri+hs+"."+file_extension
    print dest
    try:
        urllib.urlretrieve(url,dest)
    except:
        print "save failed" 
searchPic("cars") 


###imgurl= is a query, so it can be parsed, beutifulsoup returns us lots of HTML objects, we can find them easily 
### try to find the url of images we want in the html element is critical in scraping. A lot of string parsing. 
### use try and except to pass the elements that does not satisfy conditions  