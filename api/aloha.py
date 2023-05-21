from http.server import BaseHTTPRequestHandler
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        
        
        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        s = "hellow salah"
        # self.wfile.write(s.encode('utf-8'))
        return