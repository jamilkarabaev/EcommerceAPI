from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAdmin(BaseUserAdmin):


    """ admin:core_user_changelist """
    ordering = ['id']
    list_display = ['email', 'name']
    list_filter = ('is_superuser', 'is_seller')



    """ admin:core_user_change """
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal Info'), {'fields': ('name',)}),
        (('Permissions'), {'fields': ('is_active', 'is_seller', 'is_staff', 'is_superuser')})
    )


    """ admin:core_user_add """
    add_fieldsets= (
        (None, {'classes' : ('wide',),   'fields' : ('email', 'password1', 'password2', 'is_seller')}),

    )

admin.site.register(models.User, UserAdmin)


