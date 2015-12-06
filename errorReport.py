#!/usr/bin/env python

import time

currentTime = time.asctime(time.localtime(time.time()))
def errorDown(url):
    currentTime = time.asctime(time.localtime(time.time()))
    fp = open('/home/hus/Desktop/meizi/errorReportDown.txt','a+')
    fp.write(currentTime +' '+ url+'\n')
    fp.close()

def errorIndex(url,re):
    currentTime = time.asctime(time.localtime(time.time()))
    fp = open('/home/hus/Desktop/meizi/errorReportIndex.txt','a+')
    errorInformation = currentTime +' '+ url +' '+ re + '\n'
    fp.write(errorInformation)
    fp.close()

def errorFileExist(path):
    currentTime = time.asctime(time.localtime(time.time()))
    fp = open('/home/hus/Desktop/meizi/errorFileExist.txt','a+')
    message = currentTime +' '+ path + ' exist, skip\n'
    fp.write(message)
    fp.close()
def errorLoadUrl(url):
    currentTime = time.asctime(time.localtime(time.time()))
    fp = open('/home/hus/Desktop/meizi/errorLoadUrl.txt','a+')
    message = currentTime +' '+ url + ' load error \n'
    fp.write(message)
    fp.close()
def success(filepath):
    currentTime = time.asctime(time.localtime(time.time()))
    fp = open('/home/hus/Desktop/meizi/success.txt','a+')
    message = currentTime +' '+ filepath + '\n'
    fp.write(message)
    fp.close()
#errorFileExist('/home/hus/Desktop/meizi')
#errorDown('www.baidu.com')
#errorIndex('www.baidu.com','.*?')
#errorLoadUrl('www.baidu.com')
#success('www.hus.com')