from rest_framework import serializers
from .models import *

class NewsSRL(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class NotificationSRL(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        