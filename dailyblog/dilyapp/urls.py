from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name= "home"),
    path('article/', views.article_details,name= "articles"),
    path('category/',views.category,name= "category"),
]