from pyexpat import model
from django.core.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from .models import *




class UsersRegister_serializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    class Meta:
        model = User
        fields = ("id",'username', 'password'
                  , 'first_name', 'last_name', "email")
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def validate_password(self, validated_data):
        if len(validated_data) < 8:
            raise ValidationError("password need to be more than 8 character")
        return validated_data

    def validate_username(self, validated_data):
        username = validated_data
        special_characters = "!@#$%^&*()-+?=,<>/"
        if any(c in special_characters for c in username):
            raise ValidationError("Username must don't have character")
        return username.lower()

class User_retrieve_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password','email']



class Customer_panel_serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_panel
        fields = '__all__'
        