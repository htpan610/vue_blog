# article/urls.py

from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('article_list', views.article_list, name='list'),
    path('',views.home)
]