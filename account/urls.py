from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
path('User_retrieve/<str:username>/',User_retrieve.as_view(),name="User_retrieve"),#*
path('Customer_panel_retrieve/<int:code>/',Customer_panel_retrieve.as_view(),name="Customer_panel_retrieve"),
path('login/',obtain_auth_token)
]
