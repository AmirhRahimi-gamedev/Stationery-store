from django.contrib import admin
from .models import Category, Product

@admin.action(description="Deactivate selected products")
def deactivate_products(modeladmin, request, queryset):
    queryset.update(is_active=False)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title",)
    ordering = ("id",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "price", "stock", "is_active")
    list_filter = ("is_active", "category")
    search_fields = ("title",)
    ordering = ("id",)
    actions = [deactivate_products]
