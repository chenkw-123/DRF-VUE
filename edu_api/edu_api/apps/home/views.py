from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from home.models import Banner, Nav
from home.serializers import BannerModelSerializer, NavModelSerializer

#轮播图api接口
class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True, is_delete=False).order_by("-orders")
    serializer_class = BannerModelSerializer

#导航栏的api接口
class NavListAPIView(ListAPIView):
    queryset = Nav.objects.filter(is_show=True, is_delete=False).order_by("-orders")
    serializer_class = NavModelSerializer
