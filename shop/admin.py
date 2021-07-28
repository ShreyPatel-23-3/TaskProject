from django.contrib import admin
from .models import Product, Contact, Orders, OrderUpdate


class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "price")


admin.site.register(Product, ProductAdmin)

admin.site.register(Contact)

admin.site.register(Orders)

admin.site.register(OrderUpdate)

