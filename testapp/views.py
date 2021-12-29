from django.db.models import fields
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from requests.api import delete
from testapp.models import Employee
from django.core.serializers import serialize
from testapp.mixins import SerializeMixins
import json
from django.views.decorators.csrf import csrf_exempt
from testapp.utils import is_json
from testapp.forms import EmployeeForm
# Create your views here.
class EmployeeCRUD_CBV(SerializeMixins,View):
    def get_objcet_by_id(self,id):
        try:
            emp=Employee.objects.get(id=id)
        except Exception as e:
            emp=None
        return emp
    def get(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid data only'})
            return self.http_res(json_data,400)
        p_data=json.loads(data)
        id=p_data.get('id',None)
        if id is not None:
            emp=self.get_objcet_by_id(id)
            if emp is None:
                json_data=json.dumps({'msg':'No matched resource found'})
                return self.http_res(json_data,404)
            json_data=self.serialize([emp,])
            return self.http_res(json_data,200)
        qs=Employee.objects.all()
        json_data=self.serialize(qs)    
        return self.http_res(json_data,200)
    def post(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid data only'})
            return self.http_res(json_data,400)
        emp_data=json.loads(data)
        form=EmployeeForm(emp_data)
        if form.is_valid():
            form.save(commit=True)      
            json_data=json.dumps({'msg':'Created Sucessfully'})
            return self.http_res(json_data,201)  
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.http_res(json_data,400)  
    def put(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid data only'})
            return self.http_res(json_data,400)
        p_data=json.loads(data)
        id=p_data.get('id',None)
        if id is None:
            json_data=json.dumps({'msg':'To perform updation id is mandatory. Please provide id'})
            return self.http_res(json_data,400)
        emp=self.get_objcet_by_id(id)
        if emp is None:
            json_data=json.dumps({'msg':'No matched record found'})
            return self.http_res(json_data,404)
        provided_data=json.loads(data)
        original_data={
            'eno':emp.eno,
            'ename':emp.ename,
            'esal':emp.esal,
            'eaddr':emp.eaddr,
        }
        original_data.update(provided_data)
        form=EmployeeForm(original_data,instance=emp)      
        if form.is_valid():
            form.save(commit=True)      
            json_data=json.dumps({'msg':'Updated Sucessfully'})
            return self.http_res(json_data,200)  
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.http_res(json_data,400)  
    def delete(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid data only'})
            return self.http_res(json_data,400)
        p_data=json.loads(data)
        id=p_data.get('id',None)
        if id is not None:
            emp=self.get_objcet_by_id(id)
            if emp is None:
                json_data=json.dumps({'msg':'No matched resource found'})
                return self.http_res(json_data,404)
            status, deleted_item = emp.delete()
            if status==1:
                json_data=json.dumps({'msg':'Resource deleted sucessfully'})
                return self.http_res(json_data,200)
            json_data=json.dumps({'msg':'Unable to delete'})
            return self.http_res(json_data,400)
        json_data=json.dumps({'msg':'id is mandatory'})
        return self.http_res(json_data,404)

















