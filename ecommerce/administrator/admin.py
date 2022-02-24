from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
# admin.site.register(Product)
admin.site.register(ContactUs)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'brand', 'price', 'stock', 'status', 'created_on', 'updated_on']
    list_filter = ['status', 'category', 'brand']
    list_editable = ['price', 'stock', 'status','category']
    search_fields = ['name', 'category__name', 'brand__name']
    prepopulated_fields = {"slug": ("name",)}