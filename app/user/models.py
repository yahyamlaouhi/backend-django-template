from django.conf import settings
from django.db import models

from core.models import User

from .definitions import BUYER_PREFIX, SELLER_PREFIX


def create_custom_id(user_type="", user_uuid=None):
    return f"{user_type}{settings.SEPERATOR}{user_uuid}"


class Buyer(User):
    """Buyer Model"""

    number = models.CharField(blank=True, max_length=10, editable=False)

    def save(self, *args, **kwargs):
        # Save your object. After this line, value of identifier will be 0 which is default value
        super().save(*args, **kwargs)
        # Here value of identifier will be updated according to your id value
        try:
            if BUYER_PREFIX not in str(self.identifier):
                self.identifier = create_custom_id(BUYER_PREFIX, self.identifier)
            if not self.number:
                self.number = "{num:0{width}}".format(num=self.id, width=6)
        except Exception as e:
            self.delete()
            raise e

    def __str__(self) -> str:
        return super().__str__()


class Seller(User):
    """Seller Model"""

    number = models.CharField(blank=True, max_length=10, editable=False)

    def save(self, *args, **kwargs):
        # Save your object. After this line, value of identifier will be 0 which is default value
        super().save(*args, **kwargs)
        # Here value of identifier will be updated according to your id value
        try:
            if SELLER_PREFIX not in str(self.identifier):
                self.identifier = create_custom_id(SELLER_PREFIX, self.identifier)
            if not self.number:
                self.number = "{num:0{width}}".format(num=self.id, width=6)
        except Exception as e:
            self.delete()
            raise e

    def __str__(self) -> str:
        return super().__str__()
