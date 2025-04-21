from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from .models import BandPost
from .forms import BandPostForm
# from .models import Opinion

# Create your views here.
class BandPostList(generic.ListView):
    queryset = BandPost.objects.filter(status=1)
    template_name = "add_bands/index.html"
    # model = BandPost


def createBandPost(request):
    if request.method == 'POST':
        form = BandPostForm(request.POST)
        if form.is_valid():
            band = form.save(commit=False)
            band.save()       
        form = BandPostForm()
        context = {'form': form}
    return render(
        request, "add_bands/index.html", context
        )






#def my_bands(request):
    #return HttpResponse("Hello project 4 for Heroku")
#class BandPostList(generic.ListView):
    #queryset = BandPost.objects.filter(status=1)
    #template_name = "add_bands/index.html"
    #paginate_by = 6
    #model = BandPost
    #template_name = "bandpost_list.html"

#class OpionionList(generic.ListView):
 #   model = Opinion
    #queryset = Opinion.objects.filter(status=1)
  #  template_name = "add_bands/index.html"

