from django.contrib import admin

from client_order.models import ClientOrder


# Register your models here.
class ClientOrderAdmin(admin.ModelAdmin):
    list_display = (
        'client', 'due_date', 'created', 'order_status', 'processing_time', 'nr_products',
        'nr_products_completed', 'order')


admin.site.register(ClientOrder, ClientOrderAdmin)
