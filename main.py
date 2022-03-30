from email import message
import http.server
import socketserver

PORT = 3333

class Handler(http.server.simple_http_server.SimpleHTTPRequestHandler):
    def do_GET(self):
        message = "Hello World"
        self.send_response(200)
        self.end_headers()
        self.wfile.write(message.encode("utf8"))

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()