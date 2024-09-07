from django.db import models
from Category.Models.categoryModel import Category
from django.utils.text import slugify
from Product.Models.productImage import ProductImage
from Product.Models.productSizes import ProductSize


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    images = models.ManyToManyField(ProductImage, blank=True)
    sizes = models.ManyToManyField(ProductSize, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        index_together = (("id", "slug"),)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            original_slug = self.slug
            queryset = Product.objects.filter(slug=self.slug).exists()
            count = 1
            while queryset:
                self.slug = f"{original_slug}-{count}"
                queryset = Product.objects.filter(slug=self.slug).exists()
                count += 1
            super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
