from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'name',
        'sex',

        'last_login',


        'date_joined',
        'is_active',
        'is_staff',
        'is_superuser',


    )
    list_filter = (
        'last_login',
        'is_superuser',
        'date_joined',
        'is_active',
        'is_staff',
    )
    raw_id_fields = ('groups', 'user_permissions')
