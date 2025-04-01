from django.shortcuts import render
#from django.http import HttpResponse
from django.views import generic
from .models import BandPost
#from .models import Opinion

# Create your views here.
#def my_bands(request):
    #return HttpResponse("Hello project 4 for Heroku")
class BandPostList(generic.ListView):
    queryset = BandPost.objects.filter(status=1)
    template_name = "add_bands/index.html"
    paginate_by = 6
    #model = Band_Post
    #template_name = "bandpost_list.html"

#class OpionionList(generic.ListView):
    #model = Opinion
    #queryset = Opinion.objects.filter(status=1)
    #template_name = "bandpost_list.html"

