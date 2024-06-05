#Read method
import requests
import json

URL = "http://127.0.0.1:8000/student_api/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
        #python to json data
    json_data=json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)
#get_data(2) #read method

#post

def post_data():
    data = {
        'name': 'Geeta',
        'roll': 104,
        'city': 'Rampur'
    }
    #convert in json data
    json_data=json.dumps(data)
    #sending rqst
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)
#post_data()

#update

def update_data():
    data = {
        'id':5,
        'name': 'Sanjay',
        'city': 'Khejuri'
    }
    #convert in json data
    json_data=json.dumps(data)
    #sending rqst
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)
#update_data()

#Delete

def delete_data():
    data = {
        'id':8,
    }
    #convert in json data
    json_data=json.dumps(data)
    #sending rqst
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)
delete_data()


