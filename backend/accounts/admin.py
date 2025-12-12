from django.contrib import admin
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

User = get_user_model()

# remove Group from admin site
admin.site.unregister(Group)
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # what to show in the user list
    list_display = ("username", "email", "role")
    list_display_links = ("username",)

    # hide many fields in the edit page
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal information", {"fields": ("first_name", "last_name", "email", "institution", "bio", "photo", "role")}),
    )

    # hide many fields in the "Add user" page
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "role", "password1", "password2"),
        }),
    )

    search_fields = ("username", "email")
    ordering = ("id",)

