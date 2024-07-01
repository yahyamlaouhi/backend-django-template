import uuid

from django.conf import settings
from django.db import models

from item.models import Item
from user.models import Buyer, Seller


class Order(models.Model):
    """Order model to be created by customer and consulted by restaurent"""

    STATUS = [
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Cancelled", "Cancelled"),
        ("completed", "completed"),
        ("Returned", "Returned"),
        ("Delivered", "Delivered"),
    ]

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    buyer = models.ForeignKey(
        Buyer, on_delete=models.CASCADE, related_name="order_buyer"
    )
    seller = models.ForeignKey(
        Seller, on_delete=models.CASCADE, related_name="order_seller"
    )
    address = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True, null=True)

    total_paid = models.DecimalField(max_digits=5, decimal_places=2)

    currency = models.CharField(max_length=20, default=settings.CURRENCY["TND"])

    status = models.CharField(max_length=50, choices=STATUS, default="Pending")

    class Meta:
        ordering = ("-created_at",)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name="order_items", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.id} {self.item}"
