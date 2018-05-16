from flask import Flask, request
import json

app = Flask(__name__)

data = {'alex':'provencher'}

#######################
#skeleton for rest API 
#######################
error = 'invalid key something went worng',400


@app.route('/', methods=['GET'])
def api_get():
        return json.dumps(data) # GET operator, allow for searches in objects lists


@app.route('/', methods=['POST'])
def api_post():
    request_data =  json.loads(request.data)
    for i in request_data.keys():  # create new object according to data in payload
        data[i] = request_data[i]
    return json.dumps(data) # or 200 generic answer


@app.route('/', methods=['PUT'])
def api_put():
    request_data =  json.loads(request.data)                       
    try:# exemple modify
        name = request_data['surname']
        data[name] = request_data['name']         
    except: 
        return error


@app.route('/', methods=['DELETE'])
def api_delete():
    request_data =  json.loads(request.data)                       
    deleted = {}
    try:
        for i in request_data['delete']:
            deleted[i] = data.pop(i)
        return json.dumps(deleted)
    except: #in case some keys don't exist roll back
        for i in deleted.keys():
            data[i] = deleted[i]
        return error


#!!!alternate way: less if elif 
#!!!let flask call the right function with the methods param in decorators
#@app.route('/', methods=['GET'])
#def hello2():
#    return 'hello'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
