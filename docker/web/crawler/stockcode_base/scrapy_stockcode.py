#!/urs/bin/python
# -*- coding: utf-8 -*-
import re
import urllib
import sys

reload(sys)
sys.setdefaultencoding('gb18030')

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read().encode('utf-8')
    return html

def getURL(html):
    reg = r'href="(.+?\.html)" title'
    htmlgre = re.compile(reg)
    htmllist = re.findall(htmlgre,html)
    return htmllist     
def getStockCode(html):
    reg = r'href="(.+?\.html)" title'
    htmlgre = re.compile(reg)
    htmllist = re.findall(htmlgre,html)

    reg2 =r'<a.*? title="(.*?)".*?>.*?</a>'
    htmlgre2 = re.compile(reg2)
    htmllist2 = re.findall(htmlgre2,html) 
    for html_tmp in  htmllist:
	#print (html_tmp.split('/')[4])[:-5]
	 print html_tmp[30:][:-5]
    #for html_tmp2 in htmllist2:
	#print html_tmp2
html = getHtml("http://quote.eastmoney.com/usstocklist.html")
#print getURL(html)
getStockCode(html)
