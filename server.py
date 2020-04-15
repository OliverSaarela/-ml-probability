# coding=utf-8

from http.server import BaseHTTPRequestHandler
import json
import data_server_interface


class Server(BaseHTTPRequestHandler):

        
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
    
    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        #Reads json posted to server
        #format is 
        # {
	    #   "player1": "Nadal R.",
	    #   "player2": "Federer R.",
	    #   "surface": "Hard"
        # }
        lenght = int(self.headers.get('content-length'))
        postdata = json.loads(self.rfile.read(lenght))
        
        #Make a predicton
        prediction = data_server_interface.get_prediction(postdata["player1"], postdata["player2"], postdata["surface"])
        #print(prediction)
        
        #Make to json
        posting = bytes(json.dumps(prediction), "UTF-8")
        
        #Send response

        self._set_headers() 
        self.wfile.write(posting)

    def do_GET(self):
        self.respond()

    def handle_http(self):
        response_content = ""

        cont = {
            "Json" : "test"
        }
        response_content = json.dumps(cont)

        self._set_headers()
        return bytes(response_content, "UTF-8")


    def respond(self):
        content = self.handle_http()
        self.wfile.write(content)