# -*- coding:GBK -*-
# Get Douban Number ID, using HTTPParser

from HTMLParser import HTMLParser
import urllib

TARGETNAME = 'YOURNAME'

class TitleParser(HTMLParser):
    def __init__(self):
        self.readingtitle = 0
        self.title = ''
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag == 'title': 
            self.readingtitle = 1    

    def handle_data(self, data):
        if self.readingtitle:
            self.title += data

    def showTitle(self):
        if self.title:
            print self.title

    def getDoubanID(self, num):
        if self.title:
            ks = self.title.split('\n')
            print ks[0]
            if ks[0] == TARGETNAME:
                print num

if __name__ == '__main__':
    tp = TitleParser()
    for i in range(1, 3000):
        tp = TitleParser()
        url = "http://www.douban.com/people/" + str(1881000 + i) + "/"
        tp.feed(urllib.urlopen(url).read())
        tp.getDoubanID(1880000 + i)
        print i 
