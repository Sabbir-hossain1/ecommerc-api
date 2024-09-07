from rest_framework import viewsets
from Product.Models.productModel import Product
from Product.Serializers.ProductModelSerializer import (
    ProductModelSerializer,
    ProductModelListSerializer,
    ProductModelDropDownListSerializer,
)


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return ProductModelSerializer
        if self.action == "list":
            if self.request.query_params.get("dropdown", None):
                return ProductModelDropDownListSerializer
            return ProductModelListSerializer
        return super().get_serializer_class()
