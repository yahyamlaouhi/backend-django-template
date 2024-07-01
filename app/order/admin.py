from django.contrib import admin

from .models import Order, OrderItem

# from django.utils.translation import gettext as _


class OrderAdmin(admin.ModelAdmin):
    pass


class OrderItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(OrderItem, OrderItemAdmin)

admin.site.register(Order, OrderAdmin)
