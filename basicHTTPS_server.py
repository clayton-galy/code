#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

class MainHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()

httpd = HTTPServer(('0.0.0.0', 443), MainHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile="key.pem", certfile="cert.pem", server_side=True)

httpd.serve_forever()