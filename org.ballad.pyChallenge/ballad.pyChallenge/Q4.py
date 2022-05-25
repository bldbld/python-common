#start at 12345
#middle at 92118
#new start at 46059

from HTMLParser import HTMLParser
import urllib
import string
import re

def run (num):
  urlstr= "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
  url = urlstr + str(num)
  cont = urllib.urlopen(url).read()
  m = p.findall(cont)
  print str(num)+" "+cont
  if m:
    for mi in m:
      run (string.atoi(mi))
  else :
    return
  
hp = HTMLParser()
num = 46059
p = re.compile('[0-9]+')
run (num)