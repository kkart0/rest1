from django.shortcuts import render

import requests
def home1(request):
    responces=requests.get('http://127.0.0.1:8000/movieapi/').json()
    return render(request,'home1.html',{'responces':responces})
def home(request):
    return render(request,'home.html')

# Create your views here.
