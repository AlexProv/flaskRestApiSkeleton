from flask import Flask, request
import json

app = Flask(__name__)

data = {'alex':'provencher'}

#######################
#skeleton for rest API 
#######################
@app.route('/', methods=['GET','POST','PUT','DELETE'])
def api():
    if request.method == 'GET':
        return json.dumps(data)
    newData =  json.loads(request.data)                       
    if (request.method == 'POST' or request.method == 'PUT'): #will create or update if key already exist
        for i in newData.keys():
            data[i] = newData[i]
        return json.dumps(data)

    elif request.method == 'DELETE':
        deleted = {}
        try:
            for i in newData['delete']:
                deleted[i] = data.pop(i)
            return json.dumps(deleted)
        except: #in case some keys don't exist roll back
            for i in deleted.keys():
                data[i] = deleted[i]
            return 'invalid key something went worng',400


#!!!alternate way: less if elif 
#!!!let flask call the right function with the methods param in decorators
#@app.route('/', methods=['GET'])
#def hello2():
#    return 'hello'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
