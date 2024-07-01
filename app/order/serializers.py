from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from item.models import Item
from user.models import Buyer, Seller

from .models import Order, OrderItem


class ItemsOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class BuyerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ["identifier", "first_name", "last_name"]


class SellerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ["identifier", "first_name", "last_name"]


class OrderItemSerializer(serializers.ModelSerializer):
    item = ItemsOrderSerializer(read_only=True)
    uuid = serializers.CharField(write_only=True)

    class Meta:
        model = OrderItem
        fields = ["uuid", "item", "quantity"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    buyer = BuyerOrderSerializer(read_only=True)
    seller = SellerOrderSerializer(read_only=True)
    buyer_identifier = serializers.CharField(write_only=True)
    seller_identifier = serializers.CharField(write_only=True)

    class Meta:
        model = Order
        fields = [
            "uuid",
            "buyer_identifier",
            "seller_identifier",
            "buyer",
            "seller",
            "address",
            "created_at",
            "updated_at",
            "total_paid",
            "currency",
            "status",
            "items",
        ]
        read_only_fields = ["uuid", "created_at", "updated_at"]

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        try:
            validated_data["buyer"] = Buyer.objects.get(
                identifier=validated_data.pop("buyer_identifier")
            )
        except ObjectDoesNotExist:
            raise ValueError("Buyer does not exist.")

        try:
            validated_data["seller"] = Seller.objects.get(
                identifier=validated_data.pop("seller_identifier")
            )
        except ObjectDoesNotExist:
            raise ValueError("Seller does not exist.")

        order = Order.objects.create(**validated_data)
        total_paid = 0

        if items_data:

            for item in items_data:
                try:
                    item_object = Item.objects.get(uuid=item["uuid"])
                except ObjectDoesNotExist:
                    raise ValueError("Item does not exist.")

                total_paid += item_object.price
                OrderItem.objects.create(
                    order=order,
                    item=item_object,
                    quantity=item["quantity"],
                )

        order.total_paid = total_paid
        order.save()
        return order
