#Zhao Weng web image scraping
#reference 
#getting page source with python
#http://youtube.com/creeveshft
#http://christopherreevesofficial.com
#http://twitter.com/cjreeves2011
import requests
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


        htmltext = browser.open(search)
        img_urls = []
        formatted_images = []
        soup = BeautifulSoup(htmltext)
        results = soup.findAll("img")



        
        for r in results:
            try:
                print ("hello")
                if "showPhotoGallery" in r['onclick']:
                    print("hell1")
                    r['src'].replace("mip","org")
                    img_urls.append(r['src'].replace("mip","org"))
            except:
                print "eror"        

        print img_urls
        return img_urls
    except:
        print("error scrapping")
        
 


        #for im in img_urls:
        #    refer_url = urlparse(str(im))
        #    image_f = refer_url.query.split("&")[0].replace("imgurl=","")
        #    formatted_images.append(image_f)
        #
        #return  formatted_images

#    except:
#        return []
#        
#

def savePic(url):
    hs = hashlib.sha224(url).hexdigest()
    file_extension = url.split(".")[-1]
    file_name = hs + '.'+file_extension
    
    #uri = "Desktop"      ##nothing means zweng4
    #dest = uri+hs+"."+file_extension
    IMAGE = url.rsplit('/',1)[1]
    try:
        f = open(file_name,'wb')
        f.write(requests.get(url).content)
        f.close()
    except:
        print "save failed" 

def searchPic_wrapper(url):
    for i in range(10):
        if i == 0 :
            pass
        else:
            url = url + "?&page=" + str(i+1)
        searchPic(url)
        

searchPic_wrapper("https://www.sylinzi.com/home.php") 







###imgurl= is a query, so it can be parsed, beutifulsoup returns us lots of HTML objects, we can find them easily 
### try to find the url of images we want in the html element is critical in scraping. A lot of string parsing. 
### use try and except to pass the elements that does not satisfy conditions  