# -*- coding: utf-8 -*-
'''
re--One small letter, surrounded by EXACTLY three big bodyguards on each of its sides. 
http://www.pythonchallenge.com/pc/def/equality.html
在一封信中，一个小写字母被三个大写字母环绕着，值得注意的是“EXACTLY”，意思是大写字母是有且只有三个。另外，网页的title就是re，我猜测是在提示我们要用re。不过我还是先写了个不用正则表达式的，正好可以衬托一下re的强大。
注：原消息是在html源代码的注释中，我将它保存到文件“src”中。

Created on 2011-1-31

@author: bkin
'''
import re  

def foo1 ():
    file = open ("src")  
    dist = open ("dist",'w')  
    lines = file.readlines()  
    dict = {}  
    for line in lines:  
        for i in range(3,len(line)):  
            if line[i].islower():  
                if (line[i-4].islower() and line[i-3].isupper() and line[i-2].isupper() and line[i-1].isupper() and line[i+1].isupper() and line[i+2].isupper() and line[i+3].isupper() and line[i+4].islower()):  
                    dist.write(line[i])  
    file.close()  
    dist.close()

'''使用RE''' 
def foo2():         
    file = open ("src")  
    dist = open ("dist",'w')  
    lines = file.readlines()  
    dict = {}  
    for line in lines:  
        p = re.compile('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]')  
        m = p.findall(line)  
        for i in m:  
            dist.write(i[4])  
    file.close()  
    dist.close()      
 

if __name__ == '__main__':
    pass