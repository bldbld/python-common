import sys
import urllib
import pickle

def show (pair):
  return pair[0]*pair[1]

banner = urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read()
banner = pickle.loads(banner)
for line in banner:
  print ""
  for pair in line:
    sys.stdout.write(show(pair))