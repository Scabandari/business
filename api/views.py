from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Client, RFQ, RFP
from .serializers import CategorySerializer, ProductSerializer, ClientSerializer
from .serializers import RFQSerializer, RFPSerializer
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from datetime import datetime, timedelta


class CategoryList(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self):
        pass


class ProductList(APIView):

    def get(self, request, pk):
        products = Product.objects.filter(category__pk=pk)
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self):
        pass


class ClientList(APIView):

    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# http://www.django-rest-framework.org/api-guide/serializers/#deserializing-objects   'saving instances'
class RFQView(APIView):

    def get(self, request, format=None):
        rfq_list = RFQ.objects.all()
        serializer = RFQSerializer(rfq_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RFQSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
















