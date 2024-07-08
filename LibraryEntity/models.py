from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Autor(models.Model):
    name = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    dateBirth = models.DateField()
    dateDeath = models.DateField()

class Book(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete= models.PROTECT)
    genre = models.ManyToManyField(Genre)