from Category.Models.categoryModel import Category
from rest_framework import viewsets
from Category.Serializers.CategoryModelSerializer import (
    CategoryCreateUpdateSerializer,
    CategoryListSerializer,
    CategoryRetrieveSerializer,
    CategoryDropdownSerializer,
)


class CategoryModelViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action in ["create", "update"]:
            return CategoryCreateUpdateSerializer

        if self.action == "retrieve":
            return CategoryRetrieveSerializer

        if self.action == "list":
            dropdown = self.request.query_params.get("dropdown", None)
            if dropdown:
                return CategoryDropdownSerializer
            return CategoryListSerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset
