#!/usr/bin/env python3
import http.server, socketserver, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
PORT = 4600

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving Japan app on http://localhost:{PORT}")
    httpd.serve_forever()
