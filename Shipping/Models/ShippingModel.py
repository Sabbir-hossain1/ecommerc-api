from django.db import models
from Order.Models.OrderModel import Order
from User.models import User
from django_countries.fields import CountryField


ADDRESS_CHOICES = (
    ("B", "Billing"),
    ("S", "Shipping"),
)


class Shipping(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    shipping_date = models.DateTimeField(null=True, blank=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    tracking_number = models.CharField(max_length=255, null=True, blank=True)
    shipping_status = models.CharField(
        max_length=20,
        choices=[
            ("Not Shipped", "Not Shipped"),
            ("Shipped", "Shipped"),
            ("In Transit", "In Transit"),
            ("Delivered", "Delivered"),
        ],
        default="Not Shipped",
    )


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Addresses"
