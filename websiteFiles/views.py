from django.shortcuts import render, redirect
from .api import search


# Function which will show the index.html file
def index(request):
    if request.method == "POST":
        return redirect('/result')

    return render(request, 'websiteFiles/index.html')


# Function which will show the results in result.html file
def result(request):
    repo_list = search()
    return render(request, "websiteFiles/result.html", {"repo_list": repo_list})
