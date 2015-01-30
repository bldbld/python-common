# HUB MQ Simu
import sys
import time
import os

if __name__ == '__main__':
  print 'HUB MQ Simu START!'
  max_loop = int(sys.argv[1])
  sleep_seconds = int(sys.argv[2])
  print 'Read Max Loop: %d' % max_loop
  print 'Read Sleep Seconds: %d' % sleep_seconds
  for i in range (1,max_loop+1):
    os.popen('/opt/mqm/samp/bin/amqsput   Q.BANK2CPG QMBANK < HUB_SND_HVPS.TXT')
    print 'Exec amqsput, count = %d' % i
    time.sleep(sleep_seconds) 
  print 'HUB MQ Simu EXIT!'
