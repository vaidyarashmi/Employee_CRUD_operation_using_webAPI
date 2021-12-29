import requests
import json
BASE_URL='http://127.0.0.1:8000/'
END_URL='api/'                 

# def get_resource(id=None):
#     data={}
#     if id is not None:
#         data={
#             'id':id
#         }
#     resp=requests.get(BASE_URL+END_URL,data=json.dumps(data))
#     print(resp.json())
#     print(resp.status_code)
# get_resource(1)
# get_resource()
# def create_resource():
#     new_emp={
#         'eno':3000,
#         'ename':'Baby',
#         'esal':300,
#         'eaddr':'Pune'
#     }
#     resp=requests.post(BASE_URL+END_URL,data=json.dumps(new_emp))
#     print(resp.json())
#     print(resp.status_code)
# create_resource()
# def update_resource(id=None):
#     new_emp={
#         'id':id,
#         'ename':'Raj',
#         'eaddr':'Punee'
#     }
#     resp=requests.put(BASE_URL+END_URL,data=json.dumps(new_emp))
#     print(resp.json())
#     print(resp.status_code)
# update_resource(100)
# def delete_resource(id=None):
#     data={
#         'id':id
#     }
#     resp=requests.delete(BASE_URL+END_URL,data=json.dumps(data))
#     print(resp.json())
#     print(resp.status_code)
# delete_resource(7)

