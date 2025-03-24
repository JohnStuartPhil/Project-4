from django.shortcuts import render
#from django.http import HttpResponse
from django.views import generic
from .models import Post
# Create your views here.
#def my_bands(request):
    #return HttpResponse("Hello project 4 for Heroku")
class PostList(generic.ListView):
    model = Post