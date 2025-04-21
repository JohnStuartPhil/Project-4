from django.contrib import admin
from .models import BandPost # ,Opinion
# from django_summernote.admin import SummernoteModelAdmin

# @admin.register(BandPost)
# class BandPostAdmin(SummernoteModelAdmin):

 # list_display = ('name_of_band', 'status', 'created_on')
  # search_fields = ['name_of_band', 'content']
   # list_filter = ('status', 'created_on',)
    # prepopulated_fields = {'name_of_band': ('name_of_band',)}
    # summernote_fields = ('band_review',)

# Register your models here.
admin.site.register(BandPost)
#admin.site.register(Opinion)
