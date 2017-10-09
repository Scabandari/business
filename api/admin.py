from django.contrib import admin

from .models import Category, Product, RFP, RFQ

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(RFP)
admin.site.register(RFQ)