from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.endswith('/healthchek'):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Healthcheck OK')
        elif self.path.endswith('/'):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Hello, world!')
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'eror 404')



httpd = HTTPServer(("0.0.0.0", 5000), SimpleHTTPRequestHandler)
httpd.serve_forever()