from rest_framework.views import APIView
from .models import News
from .serializers import NewsSerializer
# from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
# Return all blogs using class based

class GetNews(APIView):

    def single_news(self):
        req=News.objects.all()
        serialize=NewsSerializer(req)
        # data=JSONRenderer().render(serialize)
        return Response({"message":"Data fetched successfully!!","data":serialize.data})
        
    # def 
