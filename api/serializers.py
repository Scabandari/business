from rest_framework import serializers
from .models import Category, Product, RFQ, RFP, Client


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'price', 'category']


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class RFQSerializer(serializers.ModelSerializer):

    class Meta:
        model = RFQ
        fields = '__all__'

    def create(self, validated_data):
        return RFQ.objects.create(**validated_data)


class RFPSerializer(serializers.ModelSerializer):

    class Meta:
        model = RFP
        fields = '__all__'

    def create(self, validated_data):
        return RFP.objects.create(**validated_data)