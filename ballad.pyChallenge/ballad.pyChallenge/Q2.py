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