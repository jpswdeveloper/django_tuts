from django.urls import path 
from .views import GetNews

urlpatterns=[
    path('',GetNews.single_news)
]