from django.contrib import admin

from inventory.models import Inventory


# Register your models here.
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'last_restock')


admin.site.register(Inventory, InventoryAdmin)
