import requests
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'
import json
def get_resource(id=None):#create
    data = {}
    if id is not None:
        data = {
        'id':id
        }
    resp = requests.get(BASE_URL + END_POINT, data = json.dumps(data))
    print(resp.status_code)
    print(resp.json())
get_resource(1)

def create_resource():#post
    new_emp = {
    'eno':104,
    'ename':'Katrina',
    'esal':15000,
    'eaddr':'Delhi',
    }
    resp = requests.post(BASE_URL + END_POINT, data =json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
create_resource() 

def update_resource(id):#put
    new_emp = {
    'id':id,
    'esal':15000,
    'eaddr':'Chennai',
    }
    resp = requests.put(BASE_URL + END_POINT, data = json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
update_resource(1)
