from django.shortcuts import render
#from django.http import HttpResponse
from django.views import generic
from .models import Band_Post

# Create your views here.
#def my_bands(request):
    #return HttpResponse("Hello project 4 for Heroku")
class BandPostList(generic.ListView):
    #model = Band_Post
    queryset = Band_Post.objects.filter(status=1)
    template_name = "band_post_list.html"

