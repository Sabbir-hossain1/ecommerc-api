from django.db import models


class ProductSize(models.Model):
    size = models.CharField(max_length=50)
    additional_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )

    def __str__(self):
        return f"{self.product.name} - {self.size}"
