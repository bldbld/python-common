'''
Q2：PC----ocr recognize the characters. maybe they are in the book, but MAYBE they are in the page source.
http://www.pythonchallenge.com/pc/def/ocr.html
提示说，可能在网页源文件中，打开源文件，可以看到一大堆“}@[@%]()%+$&[(_@%+%$*^@$^!+”之类的注释。同时上面还有一行注释说find rare characters in the mess below, 就是要找那一大堆注释中比较稀少的字符。
PS：我将注释保存到文件“src”中。

Created on 2011-1-31

@author: bkin
'''
file = open ("src")  
lines = file.readlines()  
dict = {}  
key_index = []  
for line in lines:  
    for i in line:  
        if dict.has_key(i):  
            tmp = dict[i]  
            dict[i] = tmp + 1  
        else :  
            dict[i] = 1  
            key_index.append(i)  
    for key in key_index:  
        if dict[key] < 15:  
            print key  
