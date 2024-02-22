from django.contrib import admin
from .models import Order, OrderItem, Category, Product
# Register your models here.

admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Product)