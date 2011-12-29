from django.db import models
from django import forms

class Post(models.Model):
    name_ru = models.CharField(max_length=25)
    name_en = models.CharField(max_length=25)
    description = models.TextField(max_length=1000)
    seasons = models.IntegerField(max_length=40) #int
    translate = models.CharField(max_length=50) #Novafilm;Lostfilm;NewStudios
    imdb = models.CharField(max_length=100) #ratio
    kinopoisk = models.CharField(max_length=100) #ratio
    img = models.CharField(max_length=100) #url
    url = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)

class PostForm(forms.Form):
    name_ru = models.CharField(max_length=25)
    name_en = models.CharField(max_length=25)
    description = models.TextField(max_length=1000)
    seasons = models.IntegerField(max_length=10)
    imdb = models.CharField(max_length=100)
    kinopoisk = models.CharField(max_length=100)
    translate = models.CharField(max_length=50)
    img = models.CharField(max_length=100)

