from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.action(description="Set selected users region to Unknown")
def set_region_unknown(modeladmin, request, queryset):
    queryset.update(region="Unknown")

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("id", "username", "first_name", "last_name", "region", "is_staff")
    list_filter = ("is_staff", "is_superuser", "region")
    search_fields = ("username", "first_name", "last_name", "region")
    ordering = ("id",)
    actions = [set_region_unknown]

    fieldsets = BaseUserAdmin.fieldsets + (
        ("Extra", {"fields": ("region",)}),
    )
