import http.server
import socketserver

PORT = 65432

Handler = http.server.SimpleHTTPRequestHandler

<<<<<<< HEAD
with socketserver.TCPServer(("192.168.0.171", PORT), Handler) as httpd:
=======
#with 127.0.0.1 it didn't work
## had to change to local ip 192.168.0.12
with socketserver.TCPServer(("192.168.0.12", PORT), Handler) as httpd:
>>>>>>> fd4a1e138ec34a2154aaa9c59130b1543ee4da6b
    print("serving at port", PORT)
    httpd.serve_forever()
