import logging

from rest_framework import serializers

from .models import Item

LOGGER = logging.getLogger(__name__)


class ItemSerializer(serializers.ModelSerializer):
    """Serializer for Item objects"""

    class Meta:
        model = Item
        fields = "__all__"
