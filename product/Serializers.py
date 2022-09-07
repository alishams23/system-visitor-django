from dataclasses import fields
import imp
from pyexpat import model
from rest_framework import serializers
from .models import *
from account.models import *
from account.Serializers import User_retrieve_serializer,Customer_panel_serializer
from extensions.utils import jalali_converter



class Category_list_serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class Image_serializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class product_list_serializer(serializers.ModelSerializer):
    category = Category_list_serializer(many=True)
    image = Image_serializer(many=True)
    class Meta:
        model = Product
        fields = '__all__'

class Order_substitute_serializer(serializers.ModelSerializer):
    product = product_list_serializer()
    class Meta:
        model = Order_substitute
        fields = "__all__" 



class Order_serializer(serializers.ModelSerializer):
    def Jalali_converter_function(self, obj):
        return f"{jalali_converter(obj.Order_time)}"
    Order_time_jalali = serializers.SerializerMethodField("Jalali_converter_function")
    products =  Order_substitute_serializer(many=True)
    visitor = User_retrieve_serializer()
    customer = Customer_panel_serializer()
    class Meta:
        model = Order
        fields = '__all__'

class Update_order_serializers(serializers.ModelSerializer):
    class Meta:

        model = Order
        fields = ('is_payment_cash','is_payed')
