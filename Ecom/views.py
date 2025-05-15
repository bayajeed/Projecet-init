from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import AboutSerializer
from .models import About
# Create your views here.
def base(request):
    return render(request, 'base.html')
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def header(request):
    return render(request, 'header.html')
def tech(request):
    return render(request, 'tech.html')

@api_view('GET')
def about(self, request):
    all_about = About.objects.all()
    serializer = AboutSerializer(all_about, many = True)
    return Response(serializer.data, status= status.HTTP_200_OK)
    