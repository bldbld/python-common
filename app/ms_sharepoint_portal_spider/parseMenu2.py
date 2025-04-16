from ntlm import HTTPNtlmAuthHandler 
import urllib2
from urllib2 import URLError, HTTPError

class JQMenu:
    def __init__(self, pmenu1, pmenu2, pmenu3, pmenu4, pmenuEx, pmenuMark):
        self.menu1 = pmenu1
        self.menu2 = pmenu2
        self.menu3 = pmenu3
        self.menu4 = pmenu4
        self.menuEx = pmenuEx
        self.menuMark = pmenuMark

def reqPortalUrl():
    user = 'USERNAME'
    password = "PASSWORD"
    url = "http://portal/C12/Menu/default.aspx"
    print url
    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, url, user, password)
    # create the NTLM authentication handler
    auth_NTLM = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)
    # create and install the opener
    opener = urllib2.build_opener(auth_NTLM)
    urllib2.install_opener(opener) 
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

def getMenu(htmlbody):
    menu = []
    for line in htmlbody.split("\r\n"):
        if line.startswith("</SCRIPT><tr><td><TABLE ID="):
            # print line
            tabline = line.split('<TD class=\"ms-vb\" nowrap>')[1]
            # print tabline
            i = 0
            for sub in tabline.split("</TD><TD Class=\"ms-vb2\">"):
                text= sub
                if i == 0:
                    text = sub.split("</TD></TR></TABLE>")[0]
                if i < 7: # Just 7 Menu, No more
                    menu.append(text.encode("gbk","ignore"))
                i = i + 1
    return menu

if __name__ == '__main__':
    # tp = TitleParser()
    # tp.feed(reqPortalUrl())
    # tp.run()
    htmlbody = reqPortalUrl()
    menu = getMenu(htmlbody)
    if len(menu) == 0:
        print 'no'
    print menu
    
 
            
    
    
