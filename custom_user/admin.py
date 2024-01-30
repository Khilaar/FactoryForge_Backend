from django.contrib import admin

from custom_user.models import CustomUser


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('type_of_user', 'email', 'address', 'city', 'state', 'country', 'verified')


admin.site.register(CustomUser, CustomUserAdmin)
