from ..models import Genre,Book,Autor
from ..SeviceLibrary import serviceGenry
import json
import datetime

def Serialise(book):
    return "{"+f"id:{book.id} , name:{book.name} , date:{book.date} ,genry: {serviceGenry.Serialise(book.genry)}"+"}"

def SerialiseList(genres):
    jsonResult = "["
    for g in genres:
        jsonResult+=Serialise(g)+","
    jsonResult+="]"
    return jsonResult


def get(Id =0):
    if Id==0:
        return SerialiseList( Autor.objects.all())
    gen  = Autor.objects.get(id = Id)
    return gen


def Desirialise(JsonBook):
    book = Book()
    
    book.name = json.loads(JsonBook.decode())['name']
#    book.date = json.loads(JsonBook.decode())['date']
    idautor = int(json.loads(JsonBook.decode())['autorId'])    
    #autor = Autor.objects.filter(id=idautor) 
    idgenry = int(json.loads(JsonBook.decode())['genryId'])   
    date = datetime.datetime.strptime(json.loads(JsonBook.decode())['date'], '%Y-%m-%d')   
    #genry = Genre.objects.filter(id=idgenry) 
    book.genre_id =idgenry
    book.autor_id = idautor
    book.date = date
    book.save()
   # book.genre.set(genry)
   # book.autor = autor;
    return book

def post(JsonBook):
    entity = Desirialise(JsonBook)
    entity.save()
    return entity