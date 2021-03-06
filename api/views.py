from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Client, RFQ, RFP
from .serializers import CategorySerializer, ProductSerializer, ClientSerializer
from .serializers import RFQSerializer, RFPSerializer
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from datetime import date, timedelta
from .request_for_quote_pb2 import RFQ_pb, RFP_pb, Product_pb, Client_pb, Category_pb
from . import request_for_quote_pb2
from datetime import datetime


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
# This view is for JSON rest post and get
class RFQView(APIView):

    def get(self, request, format=None):
        rfq_list = RFQ.objects.all()
        serializer = RFQSerializer(rfq_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RFQSerializer(data=request.data)
        if serializer.is_valid():
            rfq = serializer.save()
            id = rfq.id
            quantity = rfq.quantity
            product_number = rfq.product_number.id
            product = Product.objects.get(pk=product_number)
            price = product.price_for_quote(quantity)
            expiration = datetime.now() + timedelta(days=14)
            rfp = RFP(RFQ_id=rfq, unit_price=price, price_expiration=expiration)
            rfp.save()
            data = {
                'RFQ_id': id,
                'unit_price': price,
                'date_created': datetime.now(),
                'price_expiration': expiration
            }
            rfp_serializer = RFPSerializer(data=data)
            if rfp_serializer.is_valid():
                rfp_serializer.save()
                return Response(rfp_serializer.data, status=status.HTTP_201_CREATED)
            return Response(rfp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# This view is for PB post and get
class RFQPbView(APIView):

    def get(self, request, format=None):
        rfq = RFQ.objects.get(pk=1)
        rfq = rfq.to_pb()
        return HttpResponse(rfq, content_type='application/octet-stream')

    def post(self, request, format=None):
        rfq = RFQ_pb.FromString(request.body)
        request_for_quote = RFQ()
        request_for_quote.from_pb(rfq)
        product_pb = rfq.product_number
        product = Product()
        product.from_pb(product_pb)
        price = product.price_for_quote(rfq.quantity)
        date_time = datetime.now()
        expiration_date = date_time + timedelta(days=14)
        rfp = RFP(RFQ_id=request_for_quote, price_expiration=expiration_date, unit_price=price)
        return HttpResponse(rfp.to_pb(), content_type="application/octet-stream")



















