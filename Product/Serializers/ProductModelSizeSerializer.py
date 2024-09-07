from rest_framework import serializers
from Product.Models.productSizes import ProductSize


class ProductSizeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = "__all__"
