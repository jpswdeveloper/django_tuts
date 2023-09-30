from rest_framework.response import Response
from django.http import Http404
from rest_framework import status,generics
from ..models import News
from ..serializers import NewsSerializer

class NewsList(generics.ListCreateAPIView):
    queryset=News.objects.all()
    serializer_class=NewsSerializer

class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=News.objects.all()
    serializer_class=NewsSerializer
    