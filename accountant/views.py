from rest_framework import generics
from .Serializers import *
from account.models import *
from account.Serializers import User_retrieve_serializer
from product.Serializers import Order_serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from product.models import Order

# Create your views here.
class Visitor_retrieve(generics.RetrieveAPIView):
    lookup_field = 'code'
    queryset = User.objects.all()
    serializer_class = User_retrieve_serializer



class Store_code_retrieve(generics.RetrieveAPIView):
    queryset = Customer_panel.objects.all()
    lookup_field = "code"
    serializer_class = Customer_panel_serializer
   

# تمام ثبتی های ویزیتور 
class Visitor_registrations_list(generics.ListAPIView):
    serializer_class = Order_serializer

    def get_queryset(self):
        username = self.kwargs.get('username', 'Default Value if not there')
        result = Order.objects.filter(visitor__username=username,is_payed = True )
        return result

class confirm_Order(APIView):

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk', 'Default Value if not there')
        data = Order.objects.get(id=id)
        data.check_Accountants = not data.check_Accountants
        data.save()
        return Response(status=status.HTTP_200_OK)
