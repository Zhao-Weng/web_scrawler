import news_crawler



url = "http://www.baidu.com"


webtext = news_crawler.getHtmlText("http://www.baidu.com")
print webtext



 
 
 
 
 
 
 ###bug_log: too many arguments to unpack, means the left side has less vars to be assigned, for example a, b , c = 1,2,3,4, sometimes, browser object made
 ###by mechanize will cause that error when call open()
 
 ####when called from another file, mechanize may cause robot.txt problem. That is a weird problem
 ### google hides some content in their website when parsing using python