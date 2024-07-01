from django_filters.rest_framework import FilterSet

from .models import Item


class ItemFilter(FilterSet):
    class Meta:
        model = Item
        fields = {
            "name": ["icontains"],
            "price": ["gt", "lt"],
            "is_available": ["exact"],
            "seller": ["exact"],
        }
