from django.contrib import admin
from account.models import *

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.fieldsets += (
    ('فیلد های خاص من', {
        "fields": (
            'special_user',
        ),
    }),
)
class User_admin(admin.ModelAdmin):
    list_display = ( 'username','id')

admin.site.register(User, User_admin)


class Customer_panel_admin(admin.ModelAdmin):
    list_display =['pk']
    

admin.site.register(Customer_panel, admin_class=Customer_panel_admin)