# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from ser.models import Post, PostForm

def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            name_ru = form.cleaned_data['name_ru']
            name_en = form.cleaned_data['name_en']
            description = form.cleaned_data['description']
            seasons = form.cleaned_data['seasons']
            translate = form.cleaned_data['translate']
            imdb = form.cleaned_data['imdb']
            kinopoisk = form.cleaned_data['kinopoisk']
            p = Post(name_ru = name_ru, name_en = name_en, description = description, seasons = seasons, translate = translate, imdb = imdb, kinoopoisk = kinopoisk)
            p.save()
            return HttpResponseRedirect('')
    else:
        form = PostForm()
    post_list = Post.objects.all().order_by('-date')
    return render_to_response('index.html', {'post': post_list, 'form': form,}, context_instance=RequestContext(request))