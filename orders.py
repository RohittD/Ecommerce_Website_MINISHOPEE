from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.views import View

from store.middlewares.auth import auth_middleware
from store.models.customer import Customer
from store.models.orders import Order
from store.models.product import Products


class OrderView(View):


    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request , 'orders.html'  , {'orders' : orders})
