from django.shortcuts import render

# Create your views here.

# Function which will show the index.html file


def index(request):
    return render(request, 'websiteFiles/index.html')

# Function which will show the result.html file


def result(request):
    return render(request, "websiteFiles/result.html")
