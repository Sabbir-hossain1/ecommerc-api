from django.db import models
from User.models import User
from Order.Models.CouponModel import Coupon
import uuid


class Order(models.Model):
    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("Pending", "Pending"),
            ("Processing", "Processing"),
            ("Shipped", "Shipped"),
            ("Delivered", "Delivered"),
            ("Cancelled", "Cancelled"),
        ],
        default="Pending",
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, blank=True, null=True)
    shipping_address = models.TextField()

    def __str__(self):
        return f"Order {self.id} by {self.customer}"
