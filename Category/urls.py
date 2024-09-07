from rest_framework.routers import DefaultRouter
from Category.Views.CategoryModelViewSet import CategoryModelViewSet
from django.urls import path, include

CategoryRouter = DefaultRouter()
CategoryRouter.register(r"categories", CategoryModelViewSet, basename="categories")

urlpatterns = [path("", include(CategoryRouter.urls))]
