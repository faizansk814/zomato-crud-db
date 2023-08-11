from django.shortcuts import render, get_object_or_404
import json
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from .models import Menu

# Create your views here.


def Create(request):
    if request.method == "POST":
        body = json.loads(request.body)
        dishname = body["dishname"]
        price = body["price"]
        available = body["available"]
        menu = Menu.objects.create(dishname=dishname, price=price, available=available)
    else:
        return HttpResponse(json.dumps({"msg": "wrong routes"}))
    return HttpResponse(json.dumps({"msg": "Data Posted succesfully"}))


def Get(req):
    menu = Menu.objects.all()
    arr = {"data": list(menu.values())}
    return JsonResponse(arr)


def Update(request, itemid):
    itemid=int(itemid)
    if request.method == "PATCH":
        menu = get_object_or_404(Menu, id=itemid)
        menu.available = "yes"
        menu.save()
    else:
        return JsonResponse({"msg":"eror"})
    return JsonResponse({"msg":"Update"})


def Delete(request, itemid):
    if request.method == "DELETE":
        menu = get_object_or_404(Menu, id=itemid)
        menu.delete()
    else:
        return JsonResponse({"msg":"eror"})
    return HttpResponse(json.dumps({"msg": "Deleted"}))
