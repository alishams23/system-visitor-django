
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Customer_panel(models.Model):
    code = models.IntegerField(blank=True,null=True,verbose_name="کدمشتری")
    Phone_number = models.TextField(blank=True,null=True,verbose_name="شماره تماس")
    payment_invoice = models.BigIntegerField(verbose_name="صورت حساب")
    History_purchase = models.DateField(verbose_name="تاریخچه خرید")
    account_banance = models.BigIntegerField(verbose_name="مانده حساب")
    history_payment = models.DateField(verbose_name="تاریخچه پرداخت")
    addres = models.TextField(verbose_name="آدرس",blank=True,null=True)
    name_shop = models.TextField(verbose_name="نام فروشگاه",blank=True,null=True)
    first_name= models.TextField(verbose_name="نام ",blank=True,null=True)
    last_name=models.TextField(verbose_name="نام خانوادگی",blank=True,null=True)
    


    class Meta:
        verbose_name = "پنل مشتری"
        verbose_name_plural = "پنل های مشتریان"


class User(AbstractUser):
    User_type_CHOICES = (
    ('V', 'Visitor'),
    ('A', 'Accountant'),
    )

    user_type = models.CharField(max_length=1, choices=User_type_CHOICES,blank=True,null=True)
    special_user = models.DateTimeField(default=timezone.now, verbose_name="کاربر ویژه")
    customer = models.ManyToManyField(Customer_panel,blank=True)
    code = models.IntegerField(blank=True,null=True)
    def is_special_user(self):
            if self.special_user > timezone.now():
                return True
            else:
                return False
    is_special_user.boolean = True
    is_special_user.short_description = 'کاربر ویژه'


    class Meta:
        verbose_name = "یوزر"
        verbose_name_plural = "یوزرها"


    