from django.shortcuts import render

# Create your views here.

def Home (request):
    return render(request, 'home.html')


def article_details (request):
    return render(request, 'article_details.html')

def category (request):
    return render(request, 'category.html')