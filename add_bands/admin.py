from django.contrib import admin
from .models import Band_Post, Opinion
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Band_Post)
class BandPostAdmin(SummernoteModelAdmin):

    list_display = ('name_of_band', 'status', 'created_on')
    search_fields = ['name_of_band', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'name_of_band': ('name_of_band',)}
    summernote_fields = ('band_review',)

# Register your models here.
#admin.site.register(Band_Post)
admin.site.register(Opinion)
