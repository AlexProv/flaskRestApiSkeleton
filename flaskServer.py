from flask import Flask, request
import json

app = Flask(__name__)

data = {'alex':'provencher'}

#######################
#skeleton for rest API 
#######################
error = 'invalid key something went worng',400

@app.route('/', methods=['GET','POST','PUT','DELETE'])
def api():
    if request.method == 'GET': # GET operator, allow for searches in objects lists
        return json.dumps(data)

    request_data =  json.loads(request.data)                       
    if request.method == 'POST': # create new object according to data in payload
        for i in request_data.keys():
            data[i] = request_data[i]
        return json.dumps(data) # or 200 generic answer

    if request.method == 'PUT': # exemple modify
        try:
            name = request_data['surname']
            data[name] = request_data['name']         
        except: 
            return error

    elif request.method == 'DELETE': # exemple buld delete
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
