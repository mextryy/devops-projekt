from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello World - v2")

if __name__ == '__main__':
    httpd = HTTPServer(('0.0.0.0', 8080), SimpleHTTPRequestHandler)
    print("Server started on port 8080...")
    httpd.serve_forever()