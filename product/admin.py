from django.contrib import admin

from product.models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'description', 'quantity', 'price', 'production_status', 'production_cost', 'category',
        'requirements',)


admin.site.register(Product, ProductAdmin)
