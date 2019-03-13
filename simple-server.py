import http.server
import socketserver

PORT = 65432

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("192.168.0.171", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
