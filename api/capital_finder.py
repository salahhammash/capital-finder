from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        s= self.path 
        url_component = parse.urlsplit(s)
        qsl = parse.parse_qsl(url_component.query)
        dic = dict(qsl)
        country = dic.get("country")
        capital =dic.get("capital")
        
        if country :
            url =f'https://restcountries.com/v3.1/name/{country}'
            res = requests.get(url)
            data = res.json()
            req = data[0]["capital"][0]
            msg = f'The capital of {country} is {req}'
    
        
        elif capital :
            url =f'https://restcountries.com/v3.1/capital/{capital}'
            res = requests.get(url)
            data = res.json()
            res2 = data[0]["name"]["common"]
            msg = f'The country of {capital} is {res2}'
        
        else :
            msg = " Uncorrect "        
              
        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(msg.encode('utf-8'))
        return
