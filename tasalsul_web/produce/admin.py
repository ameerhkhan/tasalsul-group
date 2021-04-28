from django.contrib import admin

from .models import Product, Product_types, Product_packaging

# Register your models here.
class ProductTypesInline(admin.TabularInline):      # can also use stackedinline
    model = Product_types
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['product_name']}),
        (None, {'fields': ['product_description']}),
        # maybe try adding picture field here? Didn't work! For now..
        # (None, {'fields': ['product_banner']}),
        # (None, {'fields': ['product_thumbnail']}),
        # Would you like to add video?
    ]
    inlines= [ProductTypesInline]
    list_display = ('product_name', 'product_description')
    search_fields = ['product_name', 'product_type']


admin.site.register(Product, ProductAdmin)
# admin.site.register(Product_types)
# admin.site.register(Product_packaging)