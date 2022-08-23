import code
from operator import ge
from unicodedata import category
from rest_framework.views import APIView
from account.models import Customer_panel
from .models import*
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework import generics
from .Serializers import *
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class Product_list(generics.ListAPIView):
    serializer_class = product_list_serializer
    def get_queryset(self):
        id = self.kwargs.get('pk', 'Default Value if not there')
        return Product.objects.filter(category__id = id )



class Category_list(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = Category_list_serializer
    search_fields = ['title',]



class Order_retrieve(generics.ListAPIView):
    serializer_class = Order_serializer
    def get_queryset(self):
        id = int(self.kwargs.get('pk', 'Default Value if not there'))
        result = Order.objects.filter(is_payed = False,customer_id=id)
        
        if len(result) == 0 :
            data = Order.objects.create(customer = Customer_panel.objects.get(id=id))
            data.save()
            return Order.objects.filter(is_payed = False,customer_id=id)
        print(result)
        return result

class History_purchase_list(generics.ListAPIView): 
    serializer_class = Order_serializer

    def get_queryset(self):
        id = self.kwargs.get('pk', 'Default Value if not there')
        result = Order.objects.filter(is_payed = True,customer_id=id )
        return result


class confirmation_Buy(APIView):

    def post(self, request, format=None):
        is_payment_cash = request.data.get('is_payment_cash') 
        pk = request.data.get('pk') 
        data = Order.objects.get(id = pk)
        data.is_payment_cash = is_payment_cash
        data.is_payed = True
        data.save()
        return Response(status=status.HTTP_200_OK)
