import time
import BaseHTTPServer
import json
from urlparse import urlparse, parse_qs

HOST_NAME = 'localhost' 
PORT_NUMBER = 8000 

class HttpServer(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        # print ("PATH : " + s.path) 
        if(s.path == 'static/hello.html'):
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            s.wfile.write("HELLO")
        else:
            if( 'static/variables.html' in s.path ):
                query_components = parse_qs(urlparse(s.path).query)
                s.send_response(200)
                s.send_header("Content-type", "text/html")
                for key in s.headers.keys():
                    s.send_header(key,s.headers[key])
                s.end_headers()
                s.wfile.write("VARIABLES:" + json.dumps(query_components))
            else :
                s.send_response(200)
                s.send_header("Content-type", "text/html")
                s.end_headers()
                s.wfile.write("TESTE")

    def do_POST(s):
        print "-------------------->" + s.path
        if(s.path == 'client'):
            varLen = int(s.headers['Content-Length'])
            print varLen
            postVars = s.rfile.read(varLen)
            print postVars
            s.send_response(200)
            s.send_header("Content-type", "text/plain")
            for key in s.headers.keys():
                if(key != 'Content-length'):
                    s.send_header(key,s.headers[key])
            s.end_headers()
            s.wfile.write(postVars)
        else:
            print "ERROR"
            varLen = int(s.headers['Content-Length'])
            postVars = s.rfile.read(varLen)
            print postVars
            s.send_response(200)
            s.send_header("Content-type", "text/plain")
            for key in s.headers.keys():
                if(key != 'Content-length'):
                    s.send_header(key,s.headers[key])
            s.end_headers()
            s.wfile.write("ERROR")

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), HttpServer)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    