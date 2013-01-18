from flask import Flask
from flask import request
import json

def process(r):
	result = r.form["code"]
	time = 100
	out={"time":time,"result":result}
	
	return out


app = Flask(__name__)

@app.route("/", methods=['GET'])
def root_response():
	return "Heya<form method='post' action='/'><input type='text' name='code'/><input type='submit'/></form>"

@app.route("/", methods=['POST'])
def post_response():
	out = process(request)
	return json.dumps(out)

if __name__ == "__main__":
	app.debug = True
	app.run()
