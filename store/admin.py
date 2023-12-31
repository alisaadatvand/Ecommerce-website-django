from django.contrib import admin
from .models import Product,StockProduct
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'created_date', 'modified_date')
    prepopulated_fields = {'slug': ('product_name',)}
    
admin.site.register(Product, ProductAdmin)

admin.site.register(StockProduct)
