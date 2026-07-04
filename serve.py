"""
Coyote Pairing Station - simple HTTP server.
Web Bluetooth works on localhost (secure context) without HTTPS.
"""
import http.server
import socketserver
import webbrowser
import os

PORT = 4517
HOST = "localhost"

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        super().end_headers()

print(f"Coyote Pairing Station")
print(f"Open http://{HOST}:{PORT}")
print("Press Ctrl+C to stop.")
webbrowser.open(f"http://{HOST}:{PORT}")

with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
