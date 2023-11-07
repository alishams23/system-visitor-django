from django.contrib import admin
from product.models import *


from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin
    
from extensions.utils import jalali_converter


# Register your models here.
class product_admin(admin.ModelAdmin):
    list_display =('title','price','count','id',)
    filter_horizontal = ['category','image']
    list_filter = [
     
         "category"
    ]
    search_fields = (
        "title",
    )
    

admin.site.register(Product, admin_class=product_admin)


class Order_substitute_admin(admin.ModelAdmin):
    list_display = ('id',)
    

admin.site.register(Order_substitute, admin_class=Order_substitute_admin)

@admin.register(Order)
class Order_admin(admin.ModelAdmin):
    list_display = ('id',)
    filter_horizontal = ['products',]
    search_fields = (
        "customer__code",
        "customer__first_name",
        "customer__last_name",
    )
    list_filter = [
         "payment_method",
         "is_payed",
         "check_Accountants",
         "visitor",
         "Order_time",
         
    ]
    readonly_fields = ["persian"]
    def persian(self,obj):
        return f"زمان ثبت خرید به شمسی: {date2jalali(obj.Order_time).strftime('%y/%m/%d ')}"
    



class Image_admin(admin.ModelAdmin):
    list_display = ('id',"photo","description")
    

admin.site.register(Image, admin_class=Image_admin)



class Category_admin(admin.ModelAdmin):
    list_display = ('title','id',)
    search_fields = (
        "title",
       
    )
    

admin.site.register(Category, admin_class=Category_admin)


