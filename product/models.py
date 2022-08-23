
from itertools import product
from tabnanny import check
from django.db import models


# Create your models here.
class Image(models.Model):
    photo = models.ImageField(verbose_name="عکس")

    def __str__(self):
        return f"{self.pk}--{self.photo}"
    class Meta:
        verbose_name = "عکس"
        verbose_name_plural = "عکس ها"

class Category(models.Model):
    title = models.TextField(verbose_name="متن")

    def __str__(self):
        return f"{self.pk}--{self.title}"
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"



class Product(models.Model):
    category = models.ManyToManyField("product.Category",verbose_name="دسته بندی" ,blank=True )
    price = models.BigIntegerField(verbose_name="قیمت")
    image = models.ManyToManyField("product.Image",verbose_name="عکس",blank=True)
    title = models.TextField(verbose_name="متن")
    count = models.IntegerField(verbose_name="تعداد",default=1)
    def __str__(self):
        return f"{self.pk}--{self.title}"

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"


class Order_substitute(models.Model):
    prudact = models.ForeignKey(Product,verbose_name="محصول", on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name="تعداد",default=1)


class Order(models.Model):
    products=models.ManyToManyField(Order_substitute,blank=True)
    Order_time = models.DateTimeField(verbose_name="زمان ثبت خرید",auto_now=True)
    visitor = models.ForeignKey("account.User", on_delete=models.CASCADE,verbose_name="یوزر",blank=True,null=True)
    customer=models.ForeignKey("account.Customer_panel", on_delete=models.CASCADE,blank=True,null=True)
    is_payment_cash = models.BooleanField(default=True)
    is_payed=models.BooleanField(default=False)
    check_Accountants = models.BooleanField(default=False)

    class Meta:
        verbose_name = "سبد خرید"
        verbose_name_plural = "سبدهای خرید"








