# -*- coding: utf-8 -*-
'''
Q5：peak hell - pronounce it
http://www.pythonchallenge.com/pc/def/peak.html
通过查看源代码，得到注释信息peak hell sounds familiar ?和一个文件。
这个我真的没看懂，所以查了一下，原来pick和hell连读的话很像pickle，pickle模块用于数据连续化, 便于保存传输。
banner.p便是使用pickle.dumps()的结果，难怪我没看懂。
看到输出结果以banner命令打印结果的方式打印出来，才想到“banner.p”命名的用意。

Created on 2011-1-31

@author: bkin
'''
import sys  
import urllib  
import pickle  

def show (pair):  
    return pair[0]*pair[1]  

if __name__ == '__main__':
    banner = urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read()  
    banner = pickle.loads(banner)  
    for line in banner:  
        print ""  
        for pair in line:  
            sys.stdout.write(show(pair))  
