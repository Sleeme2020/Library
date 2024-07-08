from django.shortcuts import render
from django.urls import path,include
from .Controlers import viewsAutor,viewsBook,viewsGenry


route_toLibrary = [
    path("Book/", include(viewsBook.route_toLibraryBook)),
    path("Genry/", include(viewsGenry.route_toLibraryGenry)),
    path("Autor/", include(viewsAutor.route_toLibraryAutor)),
]

