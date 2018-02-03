from django.db import models
from pb_model.models import ProtoBufMixin
from . import request_for_quote_pb2
from django.db import models
from datetime import datetime, timedelta, tzinfo
from django.utils import timezone


class Client(ProtoBufMixin, models.Model):
    pb_model = request_for_quote_pb2.Client_pb
    business_name = models.CharField(max_length=200)

    def __str__(self):
        return self.business_name


class Category(ProtoBufMixin, models.Model):
    pb_model = request_for_quote_pb2.Category_pb
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Product(ProtoBufMixin, models.Model):
    pb_model = request_for_quote_pb2.Product_pb
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField()   # for one item
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_number = models.IntegerField()

    # need the product_number field cuz when pb arrives by POST data not inclucded without

    def __str__(self):
        return self.name

    def set_product_number(self):
        self.product_number = self.pk
        self.save()

    def price_for_quote(self, number_units):
        discount = 1
        if number_units > 9999:
            discount = .6

        elif number_units > 999:
            discount = .8

        elif number_units > 99:
            discount = .9

        elif number_units > 19:
            discount = .95

        return self.price * discount


# Request For Quote
class RFQ(ProtoBufMixin, models.Model):
    pb_model = request_for_quote_pb2.RFQ_pb
    account_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    product_number = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return "Client account: {0} Product number: {1} Product category: {2} Quantity: {3}"\
            .format(self.account_id, self.product_number, self.product_category, self.quantity)


# Response For Price
class RFP(ProtoBufMixin, models.Model):
    pb_model = request_for_quote_pb2.RFP_pb
    RFQ_id = models.ForeignKey(RFQ, on_delete=models.CASCADE)
    unit_price = models.FloatField(default=1)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    price_expiration = models.DateTimeField(default=datetime.now, blank=True)
