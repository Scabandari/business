from django.db import models

from django.db import models

# Create your models here.


class Client(models.Model):
    business_name = models.CharField(max_length=200)

    def __str__(self):
        return self.business_name


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField()   # for one item
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

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


class RFQ(models.Model):
    account_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    product_number = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return "Client account: {0} Product number: {1} Product category: {2} Quantity: {3}"\
            .format(self.account_id, self.product_number, self.product_category, self.quantity)


class RFP(models.Model):
    RFQ_id = models.ForeignKey(RFQ, on_delete=models.CASCADE)
    unit_price = models.FloatField(default=1)
    date_created = models.DateField(auto_now=False, auto_now_add=True)
    price_expiration = models.DateField()  # 2 weeks after creation of RFP
