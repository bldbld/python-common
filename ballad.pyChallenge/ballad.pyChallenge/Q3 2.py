#PythonChallenge 3
import re

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