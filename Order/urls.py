from rest_framework.routers import DefaultRouter
from Order.Views.OrderModelView import OrderModelViewSet
from django.urls import path, include

orderRouter = DefaultRouter()
orderRouter.register(r"orders", OrderModelViewSet, basename="order")

urlpatterns = [path("", include(orderRouter.urls))]
