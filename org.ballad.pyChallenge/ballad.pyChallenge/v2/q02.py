'''
Q2��PC----ocr recognize the characters. maybe they are in the book, but MAYBE they are in the page source.
http://www.pythonchallenge.com/pc/def/ocr.html
��ʾ˵����������ҳԴ�ļ��У���Դ�ļ������Կ���һ��ѡ�}@[@%]()%+$&[(_@%+%$*^@$^!+��֮���ע�͡�ͬʱ���滹��һ��ע��˵find rare characters in the mess below, ����Ҫ����һ���ע���бȽ�ϡ�ٵ��ַ���
PS���ҽ�ע�ͱ��浽�ļ���src���С�

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
