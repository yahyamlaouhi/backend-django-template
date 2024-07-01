from django.contrib import admin

from .models import (
    Buyer,
    Seller,
)

# from django.utils.translation import gettext as _


class BuyerAdmin(admin.ModelAdmin):
    pass


class SellerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Seller, SellerAdmin)

admin.site.register(Buyer, BuyerAdmin)
