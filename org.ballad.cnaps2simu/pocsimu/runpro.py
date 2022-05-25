# PBOC TopMQ Simu
# Version 1.0 Beta
# author: ballad
# update: 2012/03/09
import sys
import time
import os
import string

# Write to idfile to save current ID number
def writeFileId (curr_id):
  output = open('idfile','w')
  output.write(str(curr_id))
  output.close()
 
# Read idfile to get current ID number 
def readFileId ():
  input = open ('idfile')
  k = input.readline()
  input.close()
  return int(k)

# Generate Simu System's core ID  
def genId(curr_id, idLen):
  id_value = ''
  for k in range(0,idLen-len(curr_id)):
    id_value = id_value + '0'
  id_value = id_value + curr_id
  return id_value

# Send the msg using automatic generated ID
def sendMsg2 (max_loop, sleep_seconds, filename, idLen, qName, qmNamei, myQid):
  curr_id = readFileId ()
  reg = ''
  tmpfilename = 'tmpsimu'
  for i in range (0,idLen):
    reg = reg + '^'
  for i in range (1,max_loop+1):
    sndfile = open (filename)
    tmpfile = open (tmpfilename,'w')
    for line in sndfile.readlines():
      if (line.strip() == ''):
        break
      id = genId(str(curr_id), idLen)
      strlilne = line.replace (reg, id)
      tmpfile.write(strlilne)
    tmpfile.close()
    os.popen('topmq_puts  '+qmName+' '+qName+' 1 '+myQid+' < tmpsimu')
    print 'Exec topmq_puts, count = %d' % i
    time.sleep(sleep_seconds) 
    curr_id = curr_id + 1
    sndfile.close()
  writeFileId (curr_id)

# Send msg from file directly without generating ID  
def sendMsg1 (max_loop, sleep_seconds, filename, qName, qmName, myQid):
  for i in range (1,max_loop+1):
    os.popen('topmq_puts   '+qmName+' '+qName+' 1 '+myQid+' < '+filename)
    print 'Exec topmq_puts, count = %d' % i
    time.sleep(sleep_seconds) 

if __name__ == '__main__':
  print 'PBOC TopMQ Simu (V 1.0 Beta) Simu START!'
  max_loop = int(sys.argv[1])
  sleep_seconds = float(sys.argv[2])
  filename = sys.argv[3]
  idLen = int(sys.argv[4])
  genIdMod = int(sys.argv[5])
  qName = str(sys.argv[6]).strip()
  qmName = str(sys.argv[7]).strip()
  myQid = str(sys.argv[8]).strip()
  print 'Read Max Loop: %d' % max_loop
  print 'Read Sleep Seconds: %f' % sleep_seconds
  print 'Read send filename: %s' % filename
  print 'Read len of ID: %d' % idLen
  print 'Read ID Generate Mod: %d' % genIdMod
  print 'Read Queue Name: %s' % qName
  print 'Read QM name: %s' % qmName
  print 'Read Send Queue ID %s '% myQid
  if ( genIdMod == 1 ):
    sendMsg2 (max_loop, sleep_seconds, filename, idLen, qName, qmName, myQid)
  elif (  genIdMod == 2 ):
    sendMsg1 (max_loop, sleep_seconds, filename, qName, qmName, myQid)
  print 'PBOC TopMQ Simu EXIT!'

