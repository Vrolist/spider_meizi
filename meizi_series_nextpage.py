# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 17:13:18 2015

@author: hus
"""

import re
import urllib2
import urllib
import meizi_series_getpage
import errorReport

def loadurl(url):
    try:
        conn = urllib2.urlopen(url,data=None,timeout=5)
        html = conn.read()
        return html
    except Exception:
        errorReport.errorLoadUrl(url)
        return ''
def nextpage(url,path):
    reNextLink = "<a.*?href='(.*?)'>.*?</a>"
    reNextPage = '<div.*?id="wp_page_number.*?>.*?<ul>(.*?)</ul>'
    
    searchPathTaril = '.*/([a-z]+).*?.html'
    searchurltaril = '.*/(.*?.html)'
    searchhead = '(.*)/.*?.html'
    pathTaril = re.findall(searchPathTaril,url,re.S)
    urlTaril = re.findall(searchurltaril,url,re.S)
    urlhead = re.findall(searchhead,url,re.S)
    path = path + '/' +pathTaril[0]
    print path
    nextpageurl = []
    html = ''
    while True:
        html = loadurl(url)
        if html == '':
            print 'load', url,'error'
            continue
        else:
            break
    nextPage = re.findall(reNextPage,html,re.S)
    nextLink = re.findall(reNextLink,nextPage[0],re.S)
    nextLink.append(urlTaril[0])
    #print nextPage[0]
    nextLink = sorted(list(set(nextLink)))
    for i in nextLink:
        nextpageurl.append(urlhead[0]+"/"+i)
    for i in nextpageurl:
        print i
        meizi_series_getpage.tag_series(i,path)
    
#nextpage('http://www.meizitu.com/a/sifang.html','/home/hus/Desktop/meizitu')