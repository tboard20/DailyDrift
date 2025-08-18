from django.shortcuts import render
from .models import Article, Category

# Create your views here.

def Home (request):
    stories = Article.objects.filter(is_published=True).order_by('-pub_date')
    banner = Article.objects.filter(is_published=True).order_by('-pub_date')[:1]
    carousel_news = Article.objects.filter(is_published=True).order_by('-pub_date')[:8]
    grid_news = Article.objects.filter(is_published=True).order_by('-pub_date')[:3]
    grid = Article.objects.filter(is_published=True).order_by('-pub_date')[:4]
    all_news = Article.objects.filter(is_published=True).order_by('-pub_date')[:5]
    categories = Category.objects.all()
    sport_news = Article.objects.filter(category__name="sport", is_published=True).order_by('-pub_date')[:5]
    slider_news =  Article.objects.filter(is_published=True).order_by('-pub_date')[:5]
    return render(request, 'home.html', {'stories': stories, 'categories': categories, 'sport_news': sport_news, 'banner':banner, 'all_news':all_news, 'slider_news': slider_news, 'carousel_news':carousel_news, 'grid_news':grid_news, 'grid':grid})


def article_details (request):
    return render(request, 'article_details.html')

def category (request):
    return render(request, 'category.html')