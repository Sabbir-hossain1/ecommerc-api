from django.db import models


class ProductImage(models.Model):
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.caption}"
