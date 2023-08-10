from django.shortcuts import render
import json
from django.core import serializers
from django.http import JsonResponse,HttpResponse
from .models import Menu
# Create your views here.

def Create(request):
    if request.method=="POST":
        body=json.loads(request.body)
        id=body['id']
        dishname=body['dishname']
        price=body['price']
        available=body['available']
        menu=Menu.objects.create(_id=id,dishname=dishname,price=price,available=available)
    else:
        return HttpResponse(json.dumps({"msg":"wrong routes"}))
    return HttpResponse(json.dumps({"msg":"Data Posted succesfully"}))

def Get(req):
    menu=Menu.objects.all()
    menu_data=serializers.serialize('json',menu)
    return HttpResponse(menu_data, content_type='application/json')

def Update(request):
    # if request.method=="PATCH":
    #     body=json.loads(request.body)
    #     id=body['id']
    #     for item in arr:
    #         if item['id']==id:
    #             item['available']="yes"
    # else:
    #     return HttpResponse("Wrong route")
    return HttpResponse(json.dumps({"msg":"Updated"}))

def Delete(request):
    # if request.method=="DELETE":
    #     body=json.loads(request.body)
    #     id=body['id']
    #     for item in arr:
    #         if item['id']==id:
    #             arr.remove(item)
    # else:
    #     return HttpResponse("Wrong route")
    return HttpResponse(json.dumps({"msg":"Deleted"}))



