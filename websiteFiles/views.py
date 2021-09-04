from django.shortcuts import render
from .api import search


# Function which will show the index.html file
def index(request):
    if request.method == "POST":
        return render(request, 'websiteFiles/result.html')

    return render(request, 'websiteFiles/index.html')


# Function which will show the results in result.html file
def result(request):
    repo_name_list, repo_author_list = search()
    return render(request, "websiteFiles/result.html", {"name_list": repo_name_list, "author_list": repo_author_list})
