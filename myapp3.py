import requests
import json

URL="http://127.0.0.1:8000/student_api/"
def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
        #python to json data
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)
get_data() 