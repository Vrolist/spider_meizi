# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 17:23:07 2015

@author: hus
"""

import re
#import urllib
import urllib2
import meizi_series_nextpage
import errorReport

def loadurl(url):
    try:
        conn = urllib2.urlopen(url,data=None,timeout=5)
        html = conn.read()
        return html
    except Exception:
        errorReport.errorLoadUrl(url)
        return ''
def meizi(url,path):
    reTagContent = '<div.*?class="tags">.*?<span>(.*?)</span>'
    reTagUrl = '<a.*?href="(.*?)".*?>'
    print 'start open meiziwang'
    html = ''
    while True:
        html = loadurl(url)
        if html == '':
            print 'load', url,'error'
            continue
        else:
            break
    tagContent = re.findall(reTagContent, html, re.S)
    taglists = re.findall(reTagUrl, tagContent[0], re.S)
    taglists = sorted(list(set(taglists)))
    print 'open meiziwang over'
    #print len(taglists)
    for url in taglists:
        meizi_series_nextpage.nextpage(url,path)
        #meizi_series_getpage.tag_series(url,path)
        #print url
        
meizi('http://www.meizitu.com','/home/hus/Desktop/meizi')
errorReport.success('/home/hus/Desktop/meizi')
print 'All over success and false has been report with txt file'