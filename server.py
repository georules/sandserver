#!/usr/bin/env python
from flask import Flask, request
import json,sys,os

from straitjacket.lib import straitjacket
sjconfig = os.path.join(os.path.realpath(os.path.dirname(__file__)),"straitjacket/config")
print sjconfig
sj = straitjacket.StraitJacket(sjconfig, False)

def process(r):
	stdout,stderr,exitstatus,runtime,error = sj.run("python",r.form['code'], "", None)
	result = json.dumps({"stdout":stdout,"stderr":stderr,"exitstatus":exitstatus,"time":runtime,"error":error})
	return result

app = Flask(__name__)

@app.route("/", methods=['GET'])
def root_response():
	return "Heya<form method='post' action='/'><input type='text' name='code'/><input type='submit'/></form>"

@app.route("/", methods=['POST'])
def post_response():
	out = process(request)
	return out

if __name__ == "__main__":
	app.debug = True
	app.run()
