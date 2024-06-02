# python server that responds with file and adds a Cross-Origin-Embedder-Policy: require-corp
# Cross-Origin-Opener-Policy: same-origin headers

from http.server import HTTPServer, SimpleHTTPRequestHandler
import sys

class CORSRequestHandler(SimpleHTTPRequestHandler):

    def end_headers(self):
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        super().end_headers()

if __name__ == '__main__':
    HTTPServer(('localhost', int(sys.argv[1]) if len(sys.argv) > 1 else 8000), CORSRequestHandler).serve_forever()