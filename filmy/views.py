from django.shortcuts import render

def index(request):
    return render(request, 'prvni.html')

def druhy(request):
    return render(request, 'druhy.html')