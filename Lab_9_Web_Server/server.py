# Experiment 9: Basic Web Server using Python

import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST = "0.0.0.0"
PORT = 8000

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "website"))

server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

print("Web Server is running on port 8000...")
server.serve_forever()
