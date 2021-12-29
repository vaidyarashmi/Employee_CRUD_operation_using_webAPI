from django.http import HttpResponse
from django.core.serializers import serialize
import json

class SerializeMixins(object):
    def http_res(self,json_data,status_code):
        return HttpResponse(json_data,content_type='application/json',status=status_code)
    def serialize(self,qs):
        json_data=serialize('json',qs)
        p_data=json.loads(json_data)                                            #convert json to python
        final_list=[]
        for obj in p_data:  
            emp_data=obj['fields']
            final_list.append(emp_data)                                         #get 'fields': {'eno': 500, 'ename': 'pooja', 'esal': 100000.0, 'eaddr': 'Nagpur'}}] only
        json_data=json.dumps(final_list) 
        return json_data