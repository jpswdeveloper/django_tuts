from ..models import News
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from ..serializers import NewsSerializer

# CRUD Operation

class NewsCrud(APIView):

    """
    Get All , Create News
    """

    def get(self,request,format=None):
        allNews=News.objects.all()
        serializer=NewsSerializer(allNews,many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=NewsSerializer(data=request.data)
        print(args,kwargs,"Data",request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response('Something went wrong',status=status.HTTP_400_BAD_REQUEST)

class NewsDetail(APIView):

    # Get News by filtering data
    def get_object(self,pk,format=None):
        try:
            return News.objects.get(pk=pk)
        except News.DoesNotExist:
            raise Http404
        
    def get(self,request,pk,format=None):
        news=self.get_object(pk)
        serializer=NewsSerializer(news)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def put(self,request,pk,format=None):
        news=self.get_object(pk)
        serializer=NewsSerializer(news,data=request.data,partial=True)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return
        except:
            return Response('Something went wrong',status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        news=self.get_object(pk)
        news.delete()
        return Response('News deleted successfully !!!',status=status.HTTP_204_NO_CONTENT)