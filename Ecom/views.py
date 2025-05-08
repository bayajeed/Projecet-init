from django.shortcuts import render
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


