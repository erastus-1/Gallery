from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image
from django.db import models
import datetime as dt

# Create your views here.
def home(request):
    title = 'Welcome to Photo Appy'
    images = Image.objects.all()
    return render(request, 'all/home.html',{"title" :title, "images":images})

def about(request):
    title = 'About'
    return render(request, 'all/about.html', {"title" :title})

def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any image"
        return render(request, 'all/search.html',{"message":message})
