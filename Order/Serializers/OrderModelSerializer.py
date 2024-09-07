from rest_framework import serializers
from Order.Models.OrderModel import Order


class OrderModelCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderModelRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderModelDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderModelDropDownSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()
    value = serializers.IntegerField(source="order_id")

    class Meta:
        model = Order
        fields = ["label", "value"]

    def get_label(self, obj):
        return str(obj)
