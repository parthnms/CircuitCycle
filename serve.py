#!/usr/bin/env python3
"""
Simple local development web server for CircuitCycle website.
Usage: python serve.py [port]
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Enable caching headers and UTF-8
        self.send_header('Cache-Control', 'no-cache, must-revalidate')
        super().end_headers()

if __name__ == '__main__':
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print(f"==================================================")
        print(f" CircuitCycle Sustainability Website is running! ")
        print(f" URL: {url}")
        print(f" Press Ctrl+C to stop the server")
        print(f"==================================================")
        try:
            webbrowser.open(url)
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
