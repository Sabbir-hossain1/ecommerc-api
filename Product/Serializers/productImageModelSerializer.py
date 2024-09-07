from rest_framework import serializers
from Product.Models.productImage import ProductImage


class ProductImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"
