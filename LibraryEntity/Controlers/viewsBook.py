from django.http import HttpResponse
from datetime import *
from django.urls import path
from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseNotFound,JsonResponse,HttpResponseServerError
from django.core import serializers
from ..SeviceLibrary import serviceBook
from ..models import Book

def _index(request):
    if request.method =="GET":
       return  HttpResponse(_getAll(request))
    if request.method == "POST":
        return HttpResponse(_post(request))
    return HttpResponseBadRequest("Bad Request")

def _getAll(request):
    return serviceBook.get()

def _post(request):
    try:
        res = serviceBook.post(request.body)
        return HttpResponse(res)
    except serviceBook.ValidateExeption:
        return HttpResponseBadRequest("Validate Eror")    
    except:
        return HttpResponseServerError()

def _indexId(request,Id):
    try:
        if not Id >0:
            return HttpResponseBadRequest("Bad Request id not valid")
        if request.method =="GET":
            return  JsonResponse(_get(request,Id))
        if request.method == "PUT":
            return JsonResponse(_put(request,Id))
        if request.method == "DELETE":
            return HttpResponse(_del(request,Id))
        return HttpResponseBadRequest("Bad Request") 
    except Book.DoesNotExist:
        return HttpResponseNotFound("Жанр не найжен")
    except:
        return HttpResponseServerError() 



def _get(request,Id):    
        return serviceBook.get(Id)
   

def _put(request,Id):
    if not Id>0:
        return HttpResponseBadRequest("Bad Request")
    try:
        return HttpResponse(serviceBook.update(request.body,Id))
    except Book.DoesNotExist:
        return HttpResponseNotFound()
    except:
        return HttpResponseServerError()

def _del(request,Id):
    try:
        serviceBook.delete(Id)
        return HttpResponse()
    except Book.DoesNotExist:
        return HttpResponseNotFound()
    except:
        return HttpResponseServerError()

def _search(request):
    try:
        return HttpResponse(serviceBook.search(request.GET))
    except Book.DoesNotExist:
        return HttpResponseNotFound()
    except:
        return HttpResponseServerError()




class ViewBook():
    name = ""
    date = datetime.now()
    autorId = 0
    genreId =0





route_toLibraryBook = [
    path("", _index),
    path("<int:Id>", _indexId),
    path("search", _search),
]