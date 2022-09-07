from django.shortcuts import render
from category.models import Category

from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

class CategorySerializer (ModelSerializer):
    class Meta: 
        model = Category
        fields = '__all__'

class CategoryViewSet (ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer