#!/usr/bin/env python
from flask import Flask, request
from crossdomain import crossdomain
import json,sys,os

from straitjacket.lib import straitjacket
sjconfig = os.path.join(os.path.realpath(os.path.dirname(__file__)),"straitjacket/config")
print sjconfig
sj = straitjacket.StraitJacket(sjconfig, False)

def process(code,inp):
	stdout,stderr,exitstatus,runtime,error = sj.run("python",code, inp, None)
	result = json.dumps({"stdout":stdout,"stderr":stderr,"exitstatus":exitstatus,"time":runtime,"error":error})
	return result

app = Flask(__name__)

@app.route("/", methods=['GET'])
def root_response():
	return "Heya<form method='post' action='/'><input type='text' name='code'/><input type='submit'/></form>"

@app.route("/", methods=['POST','OPTIONS'])
@crossdomain(origin='*')
def post_response():
	code = ""
	if request.headers['Content-Type'] == 'application/json':
		code = request.json['code']
		inp = request.json['input']
	else:
		code = request.form['code']
	out = process(code,inp)
	return out

#@app.after_request
#def after_request(response):
#	response.headers.add('Access-Control-Allow-Origin', '*')
#	response.headers.add('Content-Length',
#	return response

if __name__ == "__main__":
	app.debug = True
	app.run("0.0.0.0",8080)
