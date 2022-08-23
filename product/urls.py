from django.urls import path
from .views import *


urlpatterns = [
path('product_list/<int:pk>/',Product_list.as_view(),name="list_product"),
path('Category_list/',Category_list.as_view(),name="list_category"),
path('Order_retrieve/<int:pk>/',Order_retrieve.as_view(),name="list_order"),
path('History_purchase_list/<int:pk>/',History_purchase_list.as_view(),name="list_History_purchase"),#لیست خریدهای مشتری
path('confirmation_Buy/<int:pk>/',confirmation_Buy.as_view(),name="confirmation_Buy"),
]
