from django.contrib import admin
from product.models import *
# Register your models here.
class product_admin(admin.ModelAdmin):
    list_display =('title','price','count')
    filter_horizontal = ['category','image']
    

admin.site.register(Product, admin_class=product_admin)


class Order_substitute_admin(admin.ModelAdmin):
    list_display = ('id',)
    

admin.site.register(Order_substitute, admin_class=Order_substitute_admin)

class Order_admin(admin.ModelAdmin):
    list_display = ('id',)
    

admin.site.register(Order, admin_class=Order_admin)




class Image_admin(admin.ModelAdmin):
    list_display = ('id',"photo")
    

admin.site.register(Image, admin_class=Image_admin)



class Category_admin(admin.ModelAdmin):
    list_display = ('title',)
    

admin.site.register(Category, admin_class=Category_admin)


