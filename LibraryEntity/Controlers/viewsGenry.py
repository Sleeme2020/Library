from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseNotFound,JsonResponse,HttpResponseServerError
from django.urls import path
from ..SeviceLibrary import serviceGenry
from ..models import Genre
from django.core import serializers

def _index(request):
    if request.method =="GET":
       return  HttpResponse(serializers.serialize("json",_getAll(request)))
    if request.method == "POST":
        return HttpResponse(_post(request))
    return HttpResponseBadRequest("Bad Request")

def _getAll(request):
    return serviceGenry.get()

def _post(request):
    try:
        res = serviceGenry.post(request.body)
        return HttpResponse(res)
    except serviceGenry.ValidateExeption:
        return HttpResponseBadRequest("Validate Eror-error-eror2")    
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
    except Genre.DoesNotExist:
        return HttpResponseNotFound("Жанр не найжен")
    except:
        return HttpResponseServerError() 



def _get(request,Id):    
        return serviceGenry.get(Id)
   

def _put(request,Id):
    if not Id>0:
        return HttpResponseBadRequest("Bad Request")
    try:
        return HttpResponse(serviceGenry.update(request.body,Id))
    except Genre.DoesNotExist:
        return HttpResponseNotFound()
    except:
        return HttpResponseServerError()

def _del(request,Id):
    try:
        serviceGenry.delete(Id)
        return HttpResponse()
    except Genre.DoesNotExist:
        return HttpResponseNotFound()
    except:
        return HttpResponseServerError()

def _search(request):
    try:
        return HttpResponse(serviceGenry.search(request.GET))
    except Genre.DoesNotExist:
        return HttpResponseNotFound()
    except:
        return HttpResponseServerError()


route_toLibraryGenry = [
    path("", _index),
    path("<int:Id>", _indexId),
    path("search", _search),
]
