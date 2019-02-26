from bottle import Bottle, request, response
import json
from random import randint
from datetime import datetime

app = Bottle()

filepath="/app"

@app.get('/v1/investments')
def get_i1():
	with open(filepath + "/response_v1.json", mode='r') as file_handle:
		file_content = file_handle.read()
	file_handle.close()
	d1 = json.loads(file_content)
	response.content_type = 'application/json'
	return(json.dumps(d1))

@app.get('/v2/investments')
def get_i1():
	with open(filepath + "/response_v2.json", mode='r') as file_handle:
		file_content = file_handle.read()
	file_handle.close()
	d1 = json.loads(file_content)
	response.content_type = 'application/json'
	return(json.dumps(d1))

@app.get('/v1/swagger')
def get_swagger():
        with open(filepath + "/swagger_v1.json", mode='r') as file_handle:
                file_content = file_handle.read()
        file_handle.close()
        sw = json.loads(file_content)
        return(dict(sw))

@app.get('/v2/swagger')
def get_swagger():
        with open(filepath + "/swagger_v2.json", mode='r') as file_handle:
                file_content = file_handle.read()
        file_handle.close()
        sw = json.loads(file_content)
        return(dict(sw))
