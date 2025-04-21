from . import views
from django.urls import path

urlpatterns = [
    path('', views.BandPostList.as_view(), name='home'),
]