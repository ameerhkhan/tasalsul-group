from django.contrib import admin

from .models import Product, Product_types

# Register your models here.
class ProductTypesInline(admin.TabularInline):      # can also use stackedinline
    model = Product_types
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['product_name']}),
        (None, {'fields': ['product_description']}),
    ]
    inlines= [ProductTypesInline]
    list_display = ('product_name', 'product_description')
    search_fields = ['product_name', 'product_type']


admin.site.register(Product, ProductAdmin)