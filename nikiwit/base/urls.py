from django.urls import path 
from . import views
urlpatterns = [
    path('', views. home, name="home"),
    path('posts/', views. home, name="posts"),
    path('post/', views. home, name="post"),
    path('profile/', views. home, name="profile"),
    
]
