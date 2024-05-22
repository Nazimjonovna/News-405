from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from .models import *
from .serializer import *

# Create your views here.
class CreateNewsView(APIView):
    parser_classes = (MultiPartParser, )
    @swagger_auto_schema(request_body=NewsSRL)
    def post(self, request):
        serializers = NewsSRL(data = request.data)
        if serializers.is_valid():
            serializers.save()
            notification = Notification.objects.create(text = request.data.get('title'))
            # notification.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)
        

# get all News
class GetAllNewsView(APIView):
    def get(self, request):
        serializers = NewsSRL(News.objects.all(), many = True)
        return Response(serializers.data)
    
class GetALlNewView(generics.ListAPIView):
    serializer_class = NewsSRL
    queryset = News.objects.all()


class GetOneNewsView(APIView):
    def get(self, request, id):
        new = News.objects.filter(id = id).first()
        if new:
            serializers = NewsSRL(new)
            return Response(serializers.data)
        else:
            return Response("Bunday yangilik mavjud emas")
        

# patch, delete
class DeleteNewsView(APIView):
    def delete(self, request, id):
        new = News.objects.filter(id = id).first()
        if new:
            new.delete()
            return Response("O'chdi")
        else:
            return Response("bunday yangilik yo'q")


class GetNotificationUnreadedView(APIView):
    def get(self, request):
        notification = Notification.objects.filter(is_read = False)
        serializer = NotificationSRL(notification, many = True)
        return Response(serializer.data)


class ChangeStatusNotificationView(APIView):
    def patch(self, request):
        notification = Notification.objects.filter(is_read = False)
        for notif in notification:
            notif.is_read = True
            notif.save()
        serializers = NotificationSRL(notification, many = True)
        return Response(serializers.data)








































