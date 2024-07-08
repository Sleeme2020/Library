from ..models import Genre
import json


class ValidateExeption(Exception):
    pass

def get(Id=0):
    if Id==0:
        return Genre.objects.all()
    gen  = Genre.objects.get(id = Id)
    return gen

def Serialise(genre):
    return "{"+f"id:{genre.id} , name:{genre.name}"+"}"

def SerialiseList(genres):
    jsonResult = "["
    for g in genres:
        jsonResult+=Serialise(g)+","
    jsonResult+="]"
    return jsonResult

def Desirialise(JsonGenre):
    genre = Genre()
    
    genre.name = json.loads(JsonGenre.decode())['name']

    return genre

def Validate(genry):
    if len(genry.name) >50:
        raise ValidateExeption()

def post(JsonGenre):
    entity = Desirialise(JsonGenre)
    Validate(entity)
    entity.save()
    return entity

def update(JsonGenre,Id):
    entity = Desirialise(JsonGenre)
    Validate(entity)
    gen = Genre.objects.get(id = Id)
    gen.name = entity.name
    gen.save()

def delete(Id):
    gen = Genre.objects.get(id=Id)
    gen.delete()

def search(query):
    _id = query.get("id",0)
    filt = Genre.objects.all()
    if _id>0 :
        filt = filt.filter(id = _id)
    _name = query.get("name","")
    if _name!= "":
        filt = filt.filter(name = _name)
    return SerialiseList(filt)
    