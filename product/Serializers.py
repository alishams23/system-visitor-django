from pyexpat import model
from rest_framework import serializers
from .models import *

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


class Order_serializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

