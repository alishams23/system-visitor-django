from django.urls import path
from .views import *


urlpatterns = [
path('product_list/<int:pk>/',Product_list.as_view(),name="list_product"),
path('Category_list/',Category_list.as_view(),name="list_category"),
path('Order_retrieve/<int:pk>/',Order_retrieve.as_view(),name="list_order"),
path('History_purchase_list/<int:pk>/',History_purchase_list.as_view(),name="list_History_purchase"),#لیست خریدهای مشتری
path('confirmation_Buy/<int:pk>/',confirmation_Buy.as_view(),name="confirmation_Buy"),
path('Order_retrieve_2/<int:pk>/',Order_retrieve_2.as_view(),name="Order_retrieve_2"),#ریز خرید در تاریخچه خرید
path('Update_order/<int:pk>/',Update_order.as_view(),name="Update_order"),
path('delete_order_product/<int:pk>/',delete_order_product.as_view(),name="delete_order_product"),
path('add_product_to_order/<int:customer>/<int:product>/<int:count>/',add_product_to_order.as_view(),name="add_product_to_order"),#ریز خرید در تاریخچه خرید
]
