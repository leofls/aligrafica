from django.shortcuts import render
from .models import Config

from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

class ConfigSerializer(ModelSerializer):
    class Meta:
        model = Config
        fields = '__all__'

class ConfigViewSet(ModelViewSet):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer