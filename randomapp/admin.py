from django.contrib import admin
from randomapp.models import Random
# Register your models here.


class RandomAdmin(admin.ModelAdmin):
    list_display = ['nama', 'organisasi', 'kampus', 'agama']
    search_fields = ['nama', 'organisasi', 'kampus', 'agama']
    list_filter = ['nama', 'organisasi', 'kampus', 'agama']
    list_per_page = 4
admin.site.register(Random)
    
