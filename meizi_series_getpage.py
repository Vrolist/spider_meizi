# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 13:23:05 2015

@author: hus
"""
import re
import urllib2
import meizi_page_download
import errorReport
#url = 'http://www.meizitu.com/a/5195.html'
#meizitu_download.picurl(url,'/home/hus/Desktop','1')
def loadurl(url):
    try:
        conn = urllib2.urlopen(url,data=None,timeout=5)
        html = conn.read()
        return html
    except Exception:
        errorReport.errorLoadUrl(url)
        return ''
def oneOfSeries(urllist,path):
    searchname = '.*/(.*?).html'
    current_path = '' 
    for url in urllist:
        try:
            name = re.findall(searchname,url,re.S)
            current_path = path + '/' + name[0]
            meizi_page_download.picurl(url,current_path)
            errorReport.success(url)
        except IndexError:
            errorReport.errorIndex(url, searchname)


#获得一个系列中，每页中的套图url地址
def tag_series(url,path):
    #searchname = '.*/(.*?).html'
    #name = re.findall(searchname,url,re.S)
    #path = path + '/' + name[0]
    
    reSeriesList = '<div .*?class="pic".*?>.*?<a.*?href="(.*?)".*?target.*?>'
    html = ''
    while True:
        html = loadurl(url)
        if html == '':
            print 'load', url,'error'
            continue
        else:
            break
    seriesList = re.findall(reSeriesList,html,re.S)
    if len(seriesList) ==0:
        errorReport.errorIndex(url, reSeriesList)
    else:
        oneOfSeries(seriesList,path)
    

#tag_series('http://www.meizitu.com/a/sifang.html','/home/hus/Desktop')