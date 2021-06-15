from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
import datetime

# Create your models here.
class CustomUser(AbstractUser):
    user_type_choices = (
        (1,"Admin"),
        (2,"Staff"),
        (3,"Merchant"),
        (4,"Customers")
    )
    user_type = models.IntegerField(choices=user_type_choices,default=1)
    is_active = models.IntegerField(default=1)
    class Meta:
        verbose_name = 'App Staff'
        verbose_name_plural = 'App Recruits'

class AdminUser(models.Model):
    auth_user_id = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    profile_pic = models.ImageField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)
    class Meta:
        verbose_name = 'Administrator'
        verbose_name_plural = 'Administrators'

class StaffUser(models.Model):
    auth_user_id = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    profile_pic = models.FileField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)
    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Recruits'

class MerchantUser(models.Model):
    profile_pic = models.FileField(default="")
    auth_user_id = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    gst_details = models.CharField(max_length=255)
    address = models.TextField()
    is_added_by_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)
    class Meta:
        verbose_name = 'Merchant'
        verbose_name_plural = 'Merchants'

class CustomerUser(models.Model):
    profile_pic = models.FileField(default="")
    auth_user_id = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)
    class Meta:
        verbose_name = 'Consumer'
        verbose_name_plural = 'Consumers'

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    thumbnail = models.FileField()
    title = models.CharField(max_length=255)
    url_slug = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)
    def get_absolute_url(self):
        """
        This is to redirect the template to specified url name
        on submitting the form.
        """
        return reverse("category_list_view")
    
    def __str__(self):
        return self.title

class SubCategories(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Categories,on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    url_slug = models.CharField(max_length=255)
    thumbnail = models.FileField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)
    
    def get_absolute_url(self):
        """
        This is to redirect the template to specified url name
        on submitting the form.
        """
        return reverse("sub_category_list_view")

class Products(models.Model):
    id = models.AutoField(primary_key = True)
    product_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    url_slug = models.CharField(max_length=255)
    subcategories_id = models.ForeignKey(SubCategories,on_delete=models.CASCADE)
    product_max_price = models.CharField(max_length=255)
    product_discount_price = models.CharField(max_length=255)
    product_description = models.TextField()
    product_long_description = models.TextField()
    added_by_merchant = models.ForeignKey(MerchantUser,on_delete=models.CASCADE)
    in_stock_total = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

class ProductMedia(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    media_type_choices = (
        (1,"Image"),
        (2,"Video")
    )
    media_type = models.CharField(max_length=255)
    media_content = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

class ProductTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    transaction_product_count = models.IntegerField(default=1)
    transaction_type_choices = (
        (1,"Buy"),
        (2,"Sale")
    )
    transaction_type = models.CharField(choices=transaction_type_choices,max_length=255)
    transaction_description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class ProductDetails(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    title_details = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

class ProductAbout(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

class ProductTags(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

class ProductQuestions(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=255)
    answer = models.TextField()
    user_id = models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

class ProductReviews(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    review_image = models.FileField()
    rating = models.CharField(default="2.5",max_length=255)
    review = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

class ProductsReviewVoting(models.Model):
    id = models.AutoField(primary_key=True)
    product_review_id = models.ForeignKey(ProductReviews,on_delete=models.CASCADE)
    user_id_rating = models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

class ProductVarient(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class ProductVarientItems(models.Model):
    id = models.AutoField(primary_key=True)
    product_varient_id = models.ForeignKey(ProductVarient,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class CustomerOrders(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Products,on_delete=models.DO_NOTHING)
    purchase_price = models.CharField(max_length=255)
    coupon_code = models.CharField(max_length=255)
    discount_amt = models.CharField(max_length=255)
    product_status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderDelieveryStatus(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(CustomerOrders,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)
    status_message = models.CharField(max_length=255)

@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminUser.objects.create(auth_user_id=instance)
        if instance.user_type==2:
            StaffUser.objects.create(auth_user_id=instance)
        if instance.user_type==3:
            # As in merchant user the fields below passed are not default set. So they have to be passed with some value.
            MerchantUser.objects.create(auth_user_id=instance,company_name='',gst_details='',address='')
        if instance.user_type==4:
            CustomerUser.objects.create(auth_user_id=instance)

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type == 1:
        instance.adminuser.save()
    if instance.user_type == 2:
        instance.staffuser.save()
    if instance.user_type == 3:
        instance.merchantuser.save()
    if instance.user_type == 4:
        instance.customeruser.save()
