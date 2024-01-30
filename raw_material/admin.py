from django.contrib import admin

from raw_material.models import RawMaterial


# Register your models here.
class RawMaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'restock_required', 'max_quantity')


admin.site.register(RawMaterial, RawMaterialAdmin)
