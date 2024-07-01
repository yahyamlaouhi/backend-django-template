import uuid

from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _

from core.decorators import image_file_path
from user.models import Seller


@image_file_path
def item_image_file_path(_instance, _filename):
    """Generate file path for a new item image"""
    return "item"


class Item(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, null=True)
    image = models.ImageField(null=True, blank=True, upload_to=item_image_file_path)
    price = models.DecimalField(
        verbose_name=_("price"),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_available = models.BooleanField(default=True)
    seller = models.ForeignKey(Seller, on_delete=CASCADE)

    class Meta:
        ordering = ["name"]
        verbose_name = _("Item")
        verbose_name_plural = _("Items")
