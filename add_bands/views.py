from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_bands(request):
    return HttpResponse("Hello project 4 for Heroku")