from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

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


def article_details (request, slug):
    article = get_object_or_404(Article, slug=slug, is_published=True )
    categories = Category.objects.all()
    comments = article.comments.order_by('-pub_date')
    comment_form = CommentForm()
    return render(request, 'article_details.html',{'article':article, 'categories':categories,'comments':comments,'comment_form':comment_form})


    

def category (request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category=category).order_by('-pub_date')
    categories = Category.objects.all()
    return render(request, 'category.html', {'category':category, 'articles':articles, 'categories':categories})


def post_comment(request, slug):
    article = get_object_or_404(Article, slug=slug, is_published=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user if request.user.is_authenticated else None
            comment.save()
            return redirect('article_details', slug=article.slug)
    return redirect('article_details', slug=article.slug)

# def base (request):
#     article = Article.objects.filter(is_published=True).order_by('-pub_date')
#     return render(request, 'base.html',{'article':article})