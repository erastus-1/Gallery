from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image,Category
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

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Category.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all/search.html',{"message":message,"categories": searched_categories})

    else:
        message = "You haven't searched for any image"
        return render(request, 'all/search.html',{"message":message})
