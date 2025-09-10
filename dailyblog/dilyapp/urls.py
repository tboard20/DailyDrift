from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name= "home"),
    path('article/<slug:slug>/', views.article_details, name= "article_details"),
    path('category/<slug:slug>/',views.category, name= "category"),
    path('article/<slug:slug>/comment/', views.post_comment, name='post_comment'),  # New URL pattern for adding comments
]