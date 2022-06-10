from http.server import BaseHTTPRequestHandler, HTTPServer
import fibonacci
import os

hostName = '0.0.0.0'
serverPort = int(os.environ['PORT'])

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes('<html><head><title>https://pythonbasics.org</title></head>', 'utf-8'))
        self.wfile.write(bytes('<p>Fibonacci number = %s</p>'  % str(fibonacci.get_fibonacci_num(fibonacci.str_to_int(self.path))), 'utf-8'))
        self.wfile.write(bytes('<body>', 'utf-8'))
        self.wfile.write(bytes('<p>This web server calculated fibonacci number.</p>', 'utf-8'))
        self.wfile.write(bytes('</body></html>', 'utf-8'))

if __name__ == '__main__':        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print('Server started http://%s:%s' % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print('Server stopped.')
