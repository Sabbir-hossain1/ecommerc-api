from rest_framework import viewsets
from Product.Models.productSizes import ProductSize
from Product.Serializers.ProductModelSizeSerializer import ProductSizeModelSerializer


class ProductSizeModelViewSet(viewsets.ModelViewSet):
    queryset = ProductSize.objects.all()
    serializer_class = ProductSizeModelSerializer
