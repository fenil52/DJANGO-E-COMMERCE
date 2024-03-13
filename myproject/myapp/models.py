from django.db import models

from autoslug import AutoSlugField

from django.contrib.auth.models import User

# Create your models here.
class Mainslider(models.Model):
    img1=models.ImageField(upload_to='main_slider_img/')
    img2=models.ImageField(upload_to='main_slider_img/')
    img3=models.ImageField(upload_to='main_slider_img/')


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    category_img = models.ImageField(upload_to="category_img/") 
    
    def __str__(self):
        return self.category_name  
    
    def product_count(self):
        return self.allproduct_set.count() 
 


class ProductMonth(models.Model):
    month_img = models.ImageField(upload_to="product_of_month/")
    month_name = models.CharField(max_length=480)
    month_description = models.TextField(blank=True,null=True)
    month_prcie =models.PositiveIntegerField() 
    slug = AutoSlugField(populate_from="month_name",unique=True,default=None,null=True)
    
    
    
class emailbg(models.Model):
    email_img = models.ImageField(upload_to="email_section_image/")
        
class insta_post(models.Model):
    insta_post_link = models.URLField( max_length=800,blank=True,null=True,default="#")
    insta_img = models.ImageField(upload_to="instagram_images/")        


class AllProduct(models.Model):
    add_in_best_seller = models.BooleanField(default=False)
    product_img = models.ImageField(upload_to="allproduct_img")   
    product_name = models.CharField(max_length=800)
    product_price = models.PositiveIntegerField()
    product_details = models.TextField()
    category_nam = models.ForeignKey(Category,on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from="product_name",unique=True,default=None,null=True)
    extra_img1 = models.ImageField(upload_to="product_view_slider_img/", blank=True, null=True) 
    extra_img2 = models.ImageField(upload_to="product_view_slider_img/", blank=True, null=True) 
    extra_img3 = models.ImageField(upload_to="product_view_slider_img/", blank=True, null=True) 
    extra_img4 = models.ImageField(upload_to="product_view_slider_img/", blank=True, null=True) 
    extra_img5 = models.ImageField(upload_to="product_view_slider_img/", blank=True, null=True)
    
    
    def __str__(self):
        return self.product_name 

   
class Address(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    fname = models.CharField(max_length=150)   
    lname = models.CharField(max_length=150)   
    phone = models.CharField(max_length=50)   
    address = models.TextField()
    city = models.CharField(max_length=100)   
    state = models.CharField(max_length=100)   
    zipcode = models.CharField(max_length=8)
    
    def __str__(self):
        return str(self.id)
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete = models.CASCADE)   
    product = models.ForeignKey(AllProduct,on_delete =models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  
    
    def __str__ (self):
        return str(self.id)
    
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    product = models.ForeignKey(AllProduct, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Order Accept")

    def __str__(self):
        return f" User: {self.user}, Product: {self.product}, Quantity: {self.quantity}"


    
    