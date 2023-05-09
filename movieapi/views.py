from django.shortcuts import render
from os import *
from .models import *
from rest_framework import generics
from firstapp.models import Movie
from .serializers import MovieSerializers

class MovieAPIView(generics.ListCreateAPIView):
    # movie=Movie.objects.all()
    queryset=Movie.objects.all()
    serializer_class=MovieSerializers

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializers
# class MovieName(generics.ListAPIView):
    

# Create your views here.
