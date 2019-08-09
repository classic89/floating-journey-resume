from rest_framework import generics

from .models import myresume
from .serializers import Serializer
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the myresume view index.")
 
class ResumeView(viewsets.ModelViewSet):
    serializer_class = Serializer
    queryset = myresume.objects.all()


