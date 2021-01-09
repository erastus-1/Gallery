from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt

# Create your views here.
def home(request):
    return render(request, 'all/home.html')

def about(request):
    return render(request, 'all/about.html')

def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all/search.html',{"message":message})
