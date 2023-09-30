from rest_framework import mixins,status,generics
from rest_framework.response import Response
from django.http import Http404
from ..models import News
from ..serializers import NewsSerializer

class NewsCrud(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
    queryset=News.objects.all()
    serializer_class=NewsSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class NewsDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=News.objects.all()
    serializer_class=NewsSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def get(self,request,*args,**kwargs):
       return self.destroy(request,*args,**kwargs)