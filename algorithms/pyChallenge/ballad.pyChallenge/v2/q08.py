# -*- coding: utf-8 -*-
'''
Q8:working hard? - Where is the missing link?
http://www.pythonchallenge.com/pc/def/integrity.html
打开网页源文件，看到注释是加密后的用户名和密码，而图片的蜜蜂提示用bz2解密。

Created on 2011-1-31

@author: bkin
'''

if __name__ == '__main__':
    import bz2  
    un = "BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"  
    pw = "BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"  
    print bz2.decompress(un)
    print bz2.decompress(pw)  