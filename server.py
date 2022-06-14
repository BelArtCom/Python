from http.server import BaseHTTPRequestHandler, HTTPServer
import utils
import os

hostName = '0.0.0.0'
serverPort = int(os.environ['PORT'])
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/fibonacci'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(str(utils.get_fibonacci_num(int(self.path.lstrip('/fibonacci/')))), 'utf-8'))
        elif self.path.startswith('/factorial'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(str(utils.get_factorial_num(int(self.path.lstrip('/factorial/')))), 'utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes('NO DATA', 'utf-8'))

if __name__ == '__main__':        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print('Server started at http://%s:%s' % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print('Server stopped.')
