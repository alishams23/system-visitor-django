from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework import generics
from .Serializers import *
from rest_framework.authtoken.models import Token
from rest_framework import filters

# Create your views here.

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersRegister_serializer
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        token, created = Token.objects.get_or_create(user_id=response.data["id"])
        response.data["token"] = str(token)
        return response

class User_retrieve(generics.RetrieveAPIView):
    lookup_field="customer"
    queryset = User.objects.all()
    serializer_class =  User_retrieve_serializer


class Customer_panel_retrieve(generics.RetrieveAPIView):
    lookup_field="code"
    queryset = Customer_panel.objects.all()
    serializer_class = Customer_panel_serializer 
  


