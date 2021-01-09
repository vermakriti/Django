from django.shortcuts import render
from django.http import  HttpResponse
from .models import Destination

# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'kriti'})

def index(request):

    dest=Destination.objects.all()
    return render(request,'index.html',{'dest':dest})

