from django.contrib import admin

from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.product import Products


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Products,AdminProduct)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)


# username = Rohitminiproject, email = rohitminiproject@gmail.com, password = Rohit123
