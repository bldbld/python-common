# Q6 start at 90052
import string
import re

def run (num):
  filename = num+".txt"
  file = open(filename)
  cont = file.readline()
  print cont
  file.close()
  m = p.findall(cont)
  if m:
    for mi in m:
      run (mi)
  else :
    return

num = '90052'
p = re.compile('[0-9]+')
run (num)