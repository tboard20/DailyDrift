from django.shortcuts import render
from .models import Article, Category

# Create your views here.

def Home (request):
    stories = Article.objects.filter(is_published=True).order_by('-pub_date')
    categories = Category.objects.all()
    return render(request, 'home.html', {'stories': stories, 'categories': categories})


def article_details (request):
    return render(request, 'article_details.html')

def category (request):
    return render(request, 'category.html')