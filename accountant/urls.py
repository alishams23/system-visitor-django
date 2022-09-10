
from django.urls import path
from .views import *

urlpatterns = [
path('visitor_retrieve/<int:code>/',Visitor_retrieve.as_view(),name="retrieve_visitor"),
path('Store_code_retrieve/<int:code>/',Store_code_retrieve.as_view(),name="retrieve_Store_code_"),
path('Visitor_registrations_list/<str:username>/',Visitor_registrations_list.as_view(),name="Visitor_registrations_list"),
path('confirm_Order/<int:pk>/',confirm_Order.as_view(),name="confirm_Order")
]
