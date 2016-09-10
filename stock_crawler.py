import urllib
import re
import sys
import os

symbolFile = open(os.path.join(sys.path[0], "symbol.txt"), "r")
symbolList = symbolFile.read()
print symbolList
for i in symbolList:
    url = "http://finance.yahoo.com/q?s=" + i
    htmlfile = urllib.urlopen(url)     #opened object
    htmltext =htmlfile.read()         #string
    regex = '<span id="yfs_l84_' + i + '">(.+?)</span>'
    pattern = re.compile(regex)    #an object 
    price = re.findall(pattern, htmltext)
    print "the price of ",i,"is ",price[0]
    
    
    print price





###Notice: Bug_log    use 184 instead of l84, which is a problem. 
###purpose: learn regex in python, and grab the html elements to search for the stock data

###open() and import path is current working directory, which is canopy
### retrive path is default, for my computer is C:Users/zweng
### they are different from script directory 

#
#    os.getcwd() and os.path.abspath('') return the "current working directory", not the script directory.
#
#    os.path.dirname(sys.argv[0]) and os.path.dirname(__file__) return the path used to call the script, which may be relative or even blank
#    (if the script is in the cwd). Also, __file__ does not exist when the script is run in IDLE or PythonWin.
#
#    sys.path[0] and os.path.abspath(os.path.dirname(sys.argv[0])) seem to return the script directory. I'm not sure if there's any difference between these two.
