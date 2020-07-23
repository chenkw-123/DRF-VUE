from django.urls import path

from orderapp import views

urlpatterns = [
    path("options/",views.OrderAPIView.as_view())
]
