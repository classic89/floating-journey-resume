from rest_framework import generics, viewsets
from .models import MyResume
from .serializers import Serializer
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the MyResume view index.")
 
class ResumeView(viewsets.ModelViewSet):
    serializer_class = Serializer
    queryset = MyResume.objects.all()


