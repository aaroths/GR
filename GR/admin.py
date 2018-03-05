from django.contrib import admin

# Register your models here.
from .models import Intervention,Favorite

admin.site.register(Intervention)
admin.site.register(Favorite)

class InterventionAdmin(admin.ModelAdmin):
    list_display = ('number','title','image','text')
