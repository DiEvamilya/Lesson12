from django.contrib import admin

from shop.models import Category, Product, Shopp

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Shopp)