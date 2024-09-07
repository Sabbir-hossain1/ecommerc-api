from django.contrib import admin
from Order.Models.OrderModel import Order
from Order.Models.OrderItemModel import OrderItem

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)
