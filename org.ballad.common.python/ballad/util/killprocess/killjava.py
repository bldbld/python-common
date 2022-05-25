# /home/tomcat/mysbin
# Kill Java Process
# Python Script
# Ver 1.0
# Date : 20120209
import os
import sys

if __name__ == '__main__':
	kjtmp = sys.argv[1]
	print 'Temp File is %s' % kjtmp
	print 'Finding Java Process...'
	os.popen ('ps -e | grep java > ' + kjtmp)
	f = open (kjtmp)
	line = f.readline()
	ary = line.split(' ')
	if (ary[0] == ''):
		print 'No Java Process Running'
	else :
		print 'Got Java Process Number: %s' % ary[0]
		os.popen ('kill -9 ' + ary[0])
		print 'Java Process Killed'
	os.popen ('rm -f ' + kjtmp)
