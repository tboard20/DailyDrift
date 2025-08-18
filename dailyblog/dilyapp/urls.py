from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name= "home"),
    path('article/<int:id>/', views.article_details, name= "article"),
    path('category/',views.category, name= "category"),
]