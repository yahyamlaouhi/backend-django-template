from django.contrib import admin

from .models import Item

# from django.utils.translation import gettext as _


class ItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(Item, ItemAdmin)
