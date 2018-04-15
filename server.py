import http.server
import signal
import socketserver
import threading

PORT = 80
Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
s_thread = threading.Thread(target=httpd.serve_forever)
s_thread.start()
signal.signal(signal.SIGTERM, httpd.shutdown)
s_thread.join(10)
