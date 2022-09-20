from django.contrib import admin
from account.models import *

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.fieldsets += (
    ('فیلد های خاص من', {
        "fields": (
            'user_type',
            'special_user',
            'customer',
            'code',
           
        ),
    }),
)

UserAdmin.list_display += ( 'username','id')
# UserAdmin.list_filter += ('date_joined', )

admin.site.register(User, UserAdmin)



class Customer_panel_admin(admin.ModelAdmin):
    list_display =['pk']
    

admin.site.register(Customer_panel, admin_class=Customer_panel_admin)