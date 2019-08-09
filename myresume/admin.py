from django.contrib import admin
from .models import MyResume

# Register your models here.

class Admin(admin.ModelAdmin):
    list_display = ('title', 'description')
    
admin.site.register(MyResume, Admin)