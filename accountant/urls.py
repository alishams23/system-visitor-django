
from django.urls import path
from .views import *

urlpatterns = [
path('visitor_retrieve/<int:code>/',Visitor_retrieve.as_view(),name="retrieve_visitor"),
path('Store_code_retrieve/<int:code>/',Store_code_retrieve.as_view(),name="retrieve_Store_code_"),
path('Visitor_registrations_list/<int:pk>/',Visitor_registrations_list.as_view(),name="Visitor_registrations_list"),
path('is_registered/<int:pk>/',is_registered.as_view(),name="is_registered")
]
