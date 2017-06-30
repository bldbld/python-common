import urllib2
import urllib
import os
import time
import datetime
import sys
from urllib2 import URLError, HTTPError

# Get specific file from APACHE HTTP Server (only File System), and download to local DIR.
# It will ignore invalid file: the file name must like this "1313131_XX_XX_XX", the number shall be long type ,and can cast to Date.
# Date : 2017-06-16 
# Author : ballad 

# For download file
def Schedule(a,b,c):
    '''''
    a: Already download
    b: data file size 
    c: remote file size
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    #print '%.2f%%' % per

# REQ Apache
def reqApache(url):
    # url = "http://localhost/"
    print url
    req = urllib2.Request(url)
    htmlbody = ''
    try:
        response = urllib2.urlopen(req)
    except HTTPError, e:
        print 'Error code:', e.code
    except URLError, e:
        print 'Reason:', e.reason
    else:
        htmlbody = response.read()
    return htmlbody

# Parse HTML	
def parseHTML(url, localfiledir, htmlbody, validdate):
    urllist = []
    for line in htmlbody.split("\n"):
        #print line
        if line.startswith("<li>") or line.startswith("<ul><li>"):
            filename = line.split('"')[1]
            print filename
            if (isReadFile(filename , validdate) == True):
                downFile(url, filename, localfiledir)
    
    return urllist

# Download File
def downFile(url, filename, localfiledir):
    # url = "http://localhost/" + filename
    url = url + filename
    print 'read file'
    print url
    req = urllib2.Request(url)
    htmlbody = ''
    try:
        #response = urllib2.urlopen(req)
        #local = os.path.join('D:\J',filename)
        local = os.path.join(localfiledir, filename)
        urllib.urlretrieve(url,local,Schedule)
    except HTTPError, e:
        print 'Error code:', e.code
    except URLError, e:
        print 'Reason:', e.reason
    #else:
        # htmlbody = response.read()
    #return htmlbody

def isReadFile(filename, validdate):
    values = filename.split('_')
    if len(values) > 1:
        longtime = int(values[0])
        print longtime
        filedatetime = time.localtime(longtime)
        y,m,d,H,M,S = filedatetime[:6]
        filedate = datetime.datetime(y,m,d,H,M,S)
        if filedate > validdate:
            return True
    return False

if __name__ == '__main__':
    # minutes
    time_interval = int(sys.argv[1])
    validdate = datetime.datetime.now() - datetime.timedelta( minutes =+ time_interval )
    print 'Read minute interval: %d' % time_interval
    url = sys.argv[2]
    print 'Read URL: %s' % url
    localfiledir = sys.argv[3]
    print 'Read LOCALDIR: %s' % localfiledir
    htmlbody = reqApache(url)
    #menu = getMenu(htmlbody)
    #if len(menu) == 0:
    #print 'no'
    #print htmlbody
    parseHTML(url, localfiledir, htmlbody, validdate)
