# -*_ coding: utf-8 -*-
'''
Q6: now there are pairs
http://www.pythonchallenge.com/pc/def/channel.html
打开网页源文件可以看到“zip”的提示，下载得到channel.zip文件包。
我解压文件后按照readme的提示写了一段代码用于找到其中正确的数字，
得到结果“Collect the comments.”，原来答案在zip文件的注释里。
得到结果：HOCKEY，打开hockey.html，得到“it's in the air. look at the letters. ”，正确答案为“oxygen”。

Created on 2011-1-31

@author: bkin
'''
import zipfile  
import string  
import re

'''得到答案'''
def run (num):  
    filename = num+".txt"  
    comments.append(zip.getinfo(filename).comment)  
    cont = zip.read(filename)  
    m = p.findall(cont)  
    if m:  
        for mi in m:  
            run (mi)  
    else :  
        return  

'''找到提示信息“Collect the comments.'''
def getClew (num):  
    filename = num+".txt"  
    file = open(filename)  
    cont = file.readline()  
    print cont  
    file.close()  
    m = p.findall(cont)  
    if m:  
        for mi in m:  
            getClew (mi)  
    else :  
        return
 
if __name__ == '__main__':
    #找到提示信息“Collect the comments.
    num = '90052'  
    p = re.compile('[0-9]+')  
    getClew (num)
    
    #得到答案
    num = '90052'  
    comments = []  
    zip = zipfile.ZipFile("channel.zip", "r")  
    p = re.compile('[0-9]+')  
    run (num)  
    print "".join(comments)  