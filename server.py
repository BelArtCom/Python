from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

def str_to_int(string):
    return int(string.lstrip('/'))

def int_to_str(integer):
    return str(integer)

def get_fibonacci_num(fibonacci):
    fib_list = [0, 1]
    for i in range(1, fibonacci):
        fib_list_0 = fib_list[0]
        fib_list_1 = fib_list[1]
        fib_list[0] = fib_list_1
        fib_list[1] = fib_list_0 + fib_list_1
    return fib_list[1]

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes('<html><head><title>https://pythonbasics.org</title><link rel="shortcut icon" href="https://www.google.com/favicon.ico" /></head>', 'utf-8'))
        self.wfile.write(bytes('<p>Fibonacci number = %s</p>'  % int_to_str(get_fibonacci_num(str_to_int(self.path))), 'utf-8'))
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
