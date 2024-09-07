from Product.Models.productImage import ProductImage
from Product.Serializers.productImageModelSerializer import ProductImageModelSerializer
from rest_framework import viewsets


class ProductImageModelViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageModelSerializer
