from django.contrib import admin
from account.models import *
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.fieldsets += (
    ('فیلد های خاص من', {
        "fields": (
            'user_type',
            'special_user',
            'code',
           
        ),
    }),
)

# UserAdmin.list_display += ( 'username','id')
UserAdmin.list_filter += ('user_type', )

admin.site.register(User, UserAdmin)



class Customer_panel_admin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display =['pk',"name_shop","code"]
    search_fields = (
        "code",
        "first_name",
        "last_name",
    )

    
admin.site.register(Customer_panel, admin_class=Customer_panel_admin)