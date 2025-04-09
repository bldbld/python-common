# -*- coding: utf-8 -*-
'''
Q7: smarty
http://www.pythonchallenge.com/pc/def/oxygen.html
网页只有一张图片，答案在图片中间的那一条灰度。
PS:Python没有自己的图片处理模块需要安装PIL。

Created on 2011-1-31

@author: bkin
'''

import Image 
import sys 

if __name__ == '__main__':
    img = open ('file/q7_oxygen.png')  
    row = []  
    img = Image.open ('file/q7_oxygen.png')  
    for i in range(0,img.size[0],7):  
        row.append(img.getpixel((i,45)))  
    ans = []  
    for r,g,b,a in row:  
        if r == g == b:  
            ans.append(r)  
    for a in ans:  
        sys.stdout.write (chr(a))
    
    '''下面的元组是上面的输出结果得到的'''
    for s in [105, 110, 116, 101, 103, 114, 105, 116, 121]:  
        sys.stdout.write (chr(s)) 
