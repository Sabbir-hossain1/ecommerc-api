from django.contrib import admin
from Product.Models.productModel import Product
from Product.Models.productImage import ProductImage
from Product.Models.productSizes import ProductSize

admin.site.register(Product)
admin.site.register(ProductSize)
admin.site.register(ProductImage)
