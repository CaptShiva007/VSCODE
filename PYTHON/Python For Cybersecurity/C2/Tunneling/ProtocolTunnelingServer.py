from http.server import HTTPServer,BaseHTTPRequestHandler
from base64 import b64decode,b64encode

class C2Server(BaseHTTPRequestHandler):
    def do_GET(self):
        data=b64decode(self.headers["Cookie"]).decode('utf-8').rstrip()
        print("Received: %s" % data)
        if data=="C2 data":
            response=b64encode(bytes("Received",'utf-8'))
            self.send_response(200)
            self.end_headers()
            self.wfile.write(response)
        else:
            self.send_error(404)

if __name__=='__main__':
    hostname='localhost'
    port=8443
    webserver=HTTPServer((hostname,port),C2Server)
    try:
        webserver.serve_forever()
    except KeyboardInterrupt:
        pass
    webserver.server_close()
    