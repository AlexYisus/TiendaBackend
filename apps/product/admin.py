from django.contrib import admin

from apps.product.models import Product
from .models import PDFFile

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'compare_price',
                    'price', 'quantity', 'sold', )
    list_display_links = ('id', 'name', )
    list_filter = ('category', )
    list_editable = ('compare_price', 'price', 'quantity', )
    search_fields = ('name', 'description', )
    list_per_page = 25

admin.site.register(Product, ProductAdmin)

class PDFFileAdmin(admin.ModelAdmin):
    list_display = ('product', 'file', 'uploaded_at')
    search_fields = ('product__name',)

admin.site.register(PDFFile)