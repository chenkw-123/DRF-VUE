from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from orderapp.models import Order
from orderapp.serializers import OrderModelSerializer


# 生成订单的视图

class OrderAPIView(CreateAPIView):
    queryset = Order.objects.filter(is_show=True, is_delete=False)
    serializer_class = OrderModelSerializer

