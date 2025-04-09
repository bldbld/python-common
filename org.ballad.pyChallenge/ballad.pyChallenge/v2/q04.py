# -*- coding: utf-8 -*-
'''
Q4：follow the chain
http://www.pythonchallenge.com/pc/def/linkedlist.php
先点图片，然后按照网页提供的数字网页向下点，注意中间有个网页有分支。

Created on 2011-1-31

@author: bkin
'''
from HTMLParser import HTMLParser  
import urllib  
import string  
import re

def run (num):  
    urlstr = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="  
    url = urlstr + str(num)  
    cont = urllib.urlopen(url).read()  
    m = p.findall(cont)  
    print str(num) + " " + cont  
    if m:  
        for mi in m:  
            run (string.atoi(mi))  
    else :  
        return
    
'''
得到第一个结果是92118，并获得提示信息“Yes. Divide by two and keep going.” ，92118 / 2得到46059，将其设为代码中num的初始值，再运行代码，得到最终结果peak.html。
'''
if __name__ == '__main__':  
    hp = HTMLParser()  
    num = 12345  
    p = re.compile('[0-9]+')
    run (num)
