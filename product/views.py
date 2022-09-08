from django.shortcuts import render
from .models import Product

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class ProductSerializer (ModelSerializer):
    class Meta: 
        model = Product
        fields = '__all__'

class ProductList (APIView):
    def get(self, request): 
        produtos = Product.objects.all()
        serializer = ProductSerializer(produtos, many=True)

        return Response(serializer.data)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    