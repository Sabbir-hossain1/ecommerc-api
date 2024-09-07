from rest_framework.routers import DefaultRouter
from Product.Views.productModelView import ProductModelViewSet
from Product.Views.productImageView import ProductImageModelViewSet
from Product.Views.ProductSizesView import ProductSizeModelViewSet
from django.urls import path, include

ProductRouter = DefaultRouter()
ProductRouter.register(r"products", ProductModelViewSet, basename="products")

ProductImageRouter = DefaultRouter()
ProductImageRouter.register(
    r"product-images", ProductImageModelViewSet, basename="product-images"
)

ProductSizeRouter = DefaultRouter()
ProductSizeRouter.register(
    r"products-sizes", ProductSizeModelViewSet, basename="products-sizes"
)

urlpatterns = [
    path("", include(ProductRouter.urls)),
    path("", include(ProductImageRouter.urls)),
    path("", include(ProductSizeRouter.urls)),
]
