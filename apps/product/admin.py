from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity', 'sold', 'date_created')
    list_filter = ('category', 'date_created')
    search_fields = ('name',)
    readonly_fields = ('get_thumbnail',)
    fieldsets = (
        ('General Info', {
            'fields': ('name', 'photo', 'get_thumbnail', 'description', 'price', 'compare_price', 'category', 'quantity', 'sold', 'pdf_file')
        }),
        ('Dates', {
            'fields': ('date_created',),
        }),
    )