from rest_framework import serializers
from account.models import *





class Customer_panel_serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_panel
        fields = '__all__'

