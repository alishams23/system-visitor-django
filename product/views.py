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
from django.db.models import Q

# Create your views here.

class Product_list(generics.ListAPIView):
    serializer_class = product_list_serializer
    def get_queryset(self):
        id = self.kwargs.get('pk', 'Default Value if not there')
        return Product.objects.filter(Q(category__id = id) ,~Q(count = 0))



class Category_list(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = Category_list_serializer
    search_fields = ['title',]



class Order_retrieve(generics.ListAPIView):
    serializer_class = Order_serializer
    def get_queryset(self):
        id = int(self.kwargs.get('pk', 'Default Value if not there'))
        result = Order.objects.filter(is_payed = False,customer__code=id,visitor=self.request.user)
        print(result)
        if len(result) == 0 :
            data = Order.objects.create(customer = Customer_panel.objects.get(code=id),visitor=self.request.user)
            data.save()
            return Order.objects.filter(is_payed = False,customer__code=id,visitor=self.request.user)
        return result

class History_purchase_list(generics.ListAPIView): 
    serializer_class = Order_serializer

    def get_queryset(self):
        id = self.kwargs.get('pk', 'Default Value if not there')
        result = Order.objects.filter(is_payed = True,customer__code=id ).order_by('-pk')
        return result

class History_purchase_list_visitor(generics.ListAPIView): 
    serializer_class = Order_serializer

    def get_queryset(self):
        id = self.kwargs.get('pk', 'Default Value if not there')
        visitor_username = self.kwargs.get('visitor', 'Default Value if not there')
        result = Order.objects.filter(is_payed = True,customer__code=id,visitor__username = visitor_username ,  ).order_by('-pk')
        return result


class confirmation_Buy(APIView):

    def post(self, request, format=None):
        payment_method = request.data.get('payment_method') 
        pk = request.data.get('pk') 
        data = Order.objects.get(id = pk)
        data.payment_method = payment_method
        data.is_payed = True
        data.save()
        return Response(status=status.HTTP_200_OK)

class add_product_to_order(APIView):

    def get(self, request, format=None, *args, **kwargs):
        customer = self.kwargs.get('customer', 'Default Value if not there')
        product = self.kwargs.get('product', 'Default Value if not there')
        count = self.kwargs.get('count', 'Default Value if not there')
        order_data = Order.objects.filter(is_payed = False,customer__code=customer,visitor= self.request.user)
 
        if len(order_data) == 0 :  

            data = Order.objects.create(customer = Customer_panel.objects.get(code=customer),visitor=request.user)
            data.save()
            order_data = Order.objects.filter(is_payed = False,customer__code=customer)
        order_data = order_data[0]
   
        for item in order_data.products.all():
          
            if item.product.id == product:
                print('1')
                item.count += count
                item.save()
                return Response(status=status.HTTP_200_OK)
        Product_substitute_data = Product.objects.get(id=product)
        Order_substitute_data=Order_substitute.objects.create(product=Product_substitute_data,count=count)
        Order_substitute_data.save()
        order_data.products.add(Order_substitute_data)
        order_data.save()
        # decrease count of product     
        Product_substitute_data.count =  Product_substitute_data.count - count
        Product_substitute_data.save()
        return Response(status=status.HTTP_200_OK)
    

class Order_retrieve_2(generics.RetrieveAPIView):
    lookup_field = "pk"
    queryset = Order.objects.all()
    serializer_class = Order_serializer


class Update_order(generics.UpdateAPIView):
    lookup_field="pk"
    serializer_class = Update_order_serializers
    queryset = Order.objects.all()


class delete_order_product(generics.DestroyAPIView):
    lookup_field = "pk"
    serializer_class = Order_substitute_serializer
    queryset = Order_substitute.objects.all()
    def perform_destroy(self, instance):
        product_instance = instance.product
        product_instance.count +=  instance.count
        product_instance.save()
        return super().perform_destroy(instance)
