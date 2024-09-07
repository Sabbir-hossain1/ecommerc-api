from django.db import models
from Order.Models.OrderModel import Order

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(
        max_length=20,
        choices=[
            ('Credit Card', 'Credit Card'),
            ('PayPal', 'PayPal'),
            ('Stripe', 'Stripe'),
            ('Cash on Delivery', 'Cash on Delivery'),
        ],
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Completed', 'Completed'),
            ('Failed', 'Failed'),
        ],
        default='Pending',
    )

    def __str__(self):
        return f"Payment for Order {self.order.id}"
