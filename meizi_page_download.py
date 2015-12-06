# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 13:39:01 2015

@author: hus
"""
#妹子图网站，爬取单一系列图片并保存在同一个文件夹下

import urllib2
import os
import re
import errorReport

#def picCheck(path):
def loadurl(url):
    try:
        conn = urllib2.urlopen(url,data=None,timeout=5)
        html = conn.read()
        return html
    except Exception:
        errorReport.errorLoadUrl(url)
        return ''
def download(url,filename):
    try:
        conn = urllib2.urlopen(url,data=None,timeout=5)
        f = open(filename,'wb')
        f.write(conn.read())
        f.close()
        return True
    except Exception:
        print 'load',url,'error'
        return False
def save_pic(url,path):
    searchname = '.*/(.*?.jpg)'
    name = re.findall(searchname,url)
    filename = path +'/'+ name[0]
    
    #print filename + ':start'
    
    while True:
        if os.path.exists(filename):
            #os.remove(filename)
            errorReport.errorFileExist(filename)
            print filename,' exists, skip'
            return True
        elif os.path.exists(filename):
            os.mknod(filename)
        if download(url,filename):
            break
    print filename + ':over'
    errorReport.success(filename)
    
def pic_list(picList,path):
    picurl = ''
    for picurl in picList:
        save_pic(picurl,path)
        
#获得url中所有的图片url
def picurl(url,path):
    if os.path.exists(path):
        print path, 'exist'
    else:
        os.makedirs(path)
    html = ''
    while True:
        html = loadurl(url)
        if html == '':
            print 'load', url,'error'
            continue
        else:
            break
    #conn = urllib2.urlopen(url,data=None,timeout=2)
    #html = conn.read()
    rePicContent1 = '<div.*?id="picture.*?>.*?<p>(.*?)</p>'
    rePicContent2 = '<div.*?class="postContent.*?>.*?<p>(.*?)</p>'
    rePicList = '<img.*?src="(.*?)".*?>'
    picContent = re.findall(rePicContent1, html,re.S)
    if len(picContent) <=0:
        errorReport.errorIndex(url, rePicContent1)
        picContent = re.findall(rePicContent2, html,re.S)
    if len(picContent) <=0:
        errorReport.errorIndex(url, rePicContent2)
        print 'load false, over download this page and return'
        return False
    else:
        picList = re.findall(rePicList,picContent[0],re.S)
        pic_list(picList,path)
#url = 'http://www.meizitu.com/a/454.html'
#picurl(url,'/home/hus/Desktop/demo')