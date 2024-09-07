from rest_framework import serializers
from Product.Models.productModel import Product
from Category.Serializers.CategoryModelSerializer import CategoryDropdownSerializer


class ProductModelListSerializer(serializers.ModelSerializer):
    category = CategoryDropdownSerializer()

    class Meta:
        model = Product
        fields = "__all__"


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductModelDropDownListSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(source="id")
    label = serializers.CharField(source="name")

    class Meta:
        model = Product
        fields = ["value", "label"]
