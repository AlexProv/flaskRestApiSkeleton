import requests 
import json
lhost = 'http://localhost:5050/'

print 'test get'
#look up the mock database
req = requests.get(lhost)
print req.status_code
print req.json()

print ''
print 'test post'
#create entry in mock database
req = requests.post(lhost, data = json.dumps({'allo':'bollo','colo':'dolo'}))
print req.status_code
print req.json()

print ''
print 'test put'
#create entry in mock database
req = requests.put(lhost, data = json.dumps({'allo':'boooooooooollllooooooo'}))
print req.status_code
print req.json()


print ''
print 'test delete'
print 'test delete to fail'
req = requests.delete(lhost,data=json.dumps({'delete':['alex','testExist']}))
print req.status_code
print req.text
print 'test delete real'
req = requests.delete(lhost,data=json.dumps({'delete':['alex']}))
print req.status_code
print req.json()

print ''
print 'final status'
req = requests.get(lhost)
print req.status_code
print req.json()