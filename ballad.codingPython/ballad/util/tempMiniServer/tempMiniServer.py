#encoding: gbk
#author: ballad
#��ʱ���������
#������������޷�����ʱ����ʱ�����˳��򣬿��������ʾ��Ϣ����ʾ�û������޷����ʡ�
#ֻ�Ǽ򵥵���ʱ�������
import os, sys
import BaseHTTPServer
from SocketServer import ThreadingMixIn
import time
import datetime

reload(sys)
# solve  'ascii' codec can't decode byte 0xe6 in position 0
sys.setdefaultencoding("utf8")

STARTDAY = datetime.date(2015,01,20)
STARTNUM = 835
   
print ""
print '----------------------------------------------------------------------->> '
try:
    port = int(sys.argv[1])
except Exception, e:
    print '-------->> Warning: Port is not given, will use deafult port: 9777 '
    print '-------->> if you want to use other port, please execute: '
    print '-------->> python SimpleHTTPServerWithUpload.py port '
    print "-------->> port is a integer and it's range: 1024 < port < 65535 "
    port = 9999
    
if not 1024 < port < 65535:  port = 8080
serveraddr = ('', port)
print '-------->> Now, listening at port ' + str(port) + ' ...'
print '-------->> You can visit the URL:   http://localhost:' + str(port)
print '----------------------------------------------------------------------->> '
print ""
 
def modification_date(filename):
    # t = os.path.getmtime(filename)
    # return datetime.datetime.fromtimestamp(t)
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(filename)))
 
class SimpleHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    menu = []
    queryDays = {}
        
    def do_GET(self):
        """Serve a GET request."""
        self.do_Service()
 
    def do_HEAD(self):
        """Serve a HEAD request."""
        self.do_Service()
 
    def do_POST(self):
        """Serve a POST request."""
        self.do_Service()
         
    def do_Service(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("charset", "gbk")
        self.end_headers()
        k = "<body><h1 align='center'><font color='red'>�������ݿ�Ӳ��崻���ƽ̨��ʱ�޷����ʣ�Ŀǰ���ڽ��������У�ƽ̨�ָ�ʹ��ʱ������֪ͨ��</font></h1></body>"
        self.wfile.write(k)  
 
class ThreadingServer(ThreadingMixIn, BaseHTTPServer.HTTPServer):
    pass
     
def test(HandlerClass=SimpleHTTPRequestHandler,
       ServerClass=BaseHTTPServer.HTTPServer):
    BaseHTTPServer.test(HandlerClass, ServerClass)
 
if __name__ == '__main__':
    # test()
     
    # Single Thread
    # srvr = BaseHTTPServer.HTTPServer(serveraddr, SimpleHTTPRequestHandler)
     
    # Multi Thread
    srvr = ThreadingServer(serveraddr, SimpleHTTPRequestHandler)
    srvr.serve_forever()  
