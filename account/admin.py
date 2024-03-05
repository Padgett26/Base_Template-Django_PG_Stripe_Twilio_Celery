from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import Account, Profile


# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = (
        "email",
        "first_name",
        "last_name",
        "last_login",
        "is_active",
        "is_staff",
        "is_superuser",
        "date_joined",
    )
    readonly_fields = ("date_joined", "last_login")
    ordering = ("last_name",)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
admin.site.register(Profile)
