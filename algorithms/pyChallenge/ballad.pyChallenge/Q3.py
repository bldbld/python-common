#PythonChallenge Q3

file = open ("src")
dist = open ("dist",'w')
lines = file.readlines()
dict = {}
for line in lines:
  for i in range(3,len(line)):
    if line[i].islower():
      	if (line[i-4].islower() and line[i-3].isupper() and line[i-2].isupper() and line[i-1].isupper() and line[i+1].isupper() and line[i+2].isupper() and line[i+3].isupper() and line[i+4].islower()):
          dist.write(line[i])
file.close()
dist.close()     