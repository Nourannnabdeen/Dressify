from django.contrib import admin
from .models import Product, Category

class ProductInline(admin.TabularInline):
    model = Product
    extra = 1  # Number of blank inlines to show

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available_sizes', 'category', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('category', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [ProductInline]