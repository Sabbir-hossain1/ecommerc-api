from rest_framework import viewsets
from Order.Models.OrderModel import Order
from Order.Serializers.OrderModelSerializer import (
    OrderModelCreateUpdateSerializer,
    OrderModelDestroySerializer,
    OrderModelDropDownSerializer,
    OrderModelListSerializer,
    OrderModelRetrieveSerializer,
)


class OrderModelViewSet(viewsets.ModelViewSet):

    def get_queryset(self, request):
        queryset = Order.objects.all()

        return queryset

    def get_serializer_class(self, request):

        if self.action in ["create", "update", "partial_update"]:
            return OrderModelCreateUpdateSerializer
        elif self.action == "retrieve":
            return OrderModelRetrieveSerializer
        elif self.action == "destroy":
            return OrderModelDestroySerializer
        elif self.action == "list":
            if self.request.query_params.get("dropdown", None):
                return OrderModelDropDownSerializer
            return OrderModelListSerializer
