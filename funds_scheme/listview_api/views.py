from django.shortcuts import render,HttpResponse,Http404
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import funds_info
from .serializers import funds_Serializer


@csrf_exempt
def Funds_view(request):

    if request.method == 'GET':
        funds = funds_info.objects.all()
        serializer = funds_Serializer(funds,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = funds_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer,status=201)
        return JsonResponse(serializer.errors,status=400)

# Create your views here.
@csrf_exempt
def Fund_view(request,nm):
    try: 
        item = funds_info.objects.get(code = nm)
    except funds_info.DoesNotExist:
        raise Http404('Not found')
 
    if request.method == 'GET':
        serializer = funds_Serializer(item)
        return JsonResponse(serializer.data)
 
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = funds_Serializer(item,data =data)
 
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status =400)
 
    if request.method == "DELETE":
        item.delete()
        return HttpResponse(status =204)