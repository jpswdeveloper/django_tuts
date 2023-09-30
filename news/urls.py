from django.urls import path 
from  .views.class_based_api_view import NewsCrud,NewsDetail
from rest_framework.urlpatterns import format_suffix_patterns
# from .views import get_post
urlpatterns=[
    path('',NewsCrud.as_view()),    
    path('<int:pk>',NewsDetail.as_view()),    
]

urlpatterns=format_suffix_patterns(urlpatterns)