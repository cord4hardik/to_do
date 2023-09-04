from rest_framework import serializers
from .models import Todo, AccessLog

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

class AccessLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessLog
        fields = '__all__'
