from django.contrib import admin
from .models import *
from django.urls import reverse


from django.utils.html import mark_safe,format_html
# Register your models here.

# ============================  MAIN SLIDER ==========================

class SliderAdmin(admin.ModelAdmin):
    list_display = ('IMG_1','IMG_2','IMG_3')
    
    def IMG_1(self,obj):
        return mark_safe ("<img src={} height='120px' width='240px' />".format(obj.img1.url))
    
    def IMG_2(self,obj):
        return mark_safe ("<img src={} height='120px' width='240px' />".format(obj.img2.url))    

    def IMG_3(self,obj):
        return mark_safe ("<img src={} height='120px' width='240px' />".format(obj.img3.url))    

admin.site.register(Mainslider,SliderAdmin)


# ============================  CATEGORY  ==========================

class categoryAdmin(admin.ModelAdmin):
    list_display = ("cat","category_name")


    def cat(self,obj):
        return mark_safe("<img src={} height='100px' width='120px' />".format(obj.category_img.url))
    cat.short_description = "CATEGORY IMAGE"    
admin.site.register(Category,categoryAdmin)    

# ============================  ONE-MONTH-PRODUCT  ==========================

class MonthAdmin(admin.ModelAdmin):
    list_display = ("month_im", "month_name", "month_description", "month_price")

    def month_im(self, obj):
        return mark_safe("<img src={} height='100px' width='110px' />".format(obj.month_img.url))

    month_im.short_description = "ONE MONTH PRODUCT IMAGE"

    def month_name(self):
        pass
    month_name.short_description = "ONE MONTH PRODUCT NAME"

    def month_description(self, obj):
        pass
    month_description.short_description = "PRODUCT DESCRIPTION"

    def month_price(self, obj):
        pass
    month_price.short_description = "PRODUCT PRICE"
    
admin.site.register(ProductMonth,MonthAdmin)   

# ============================  EMAIL-SECTION  ==========================

class emailbgadmin(admin.ModelAdmin):
    list_display = ("bg_img",)
    
    def bg_img(self,obj):
        return mark_safe("<img src={} height='200px' width='350px'/>".format(obj.email_img.url))
    
    bg_img.short_description = "EMAIL SECTION BACKGROUND IMAGE"

admin.site.register(emailbg,emailbgadmin)    

# ============================  INSTAGRAM  ==========================

class instadmin(admin.ModelAdmin):
    list_display = ("insta_i","insta_post_link")
    
    def insta_i(self,obj):
        return mark_safe("<img src={} height='200px' width='230px' />".format(obj.insta_img.url))
    
    insta_i.short_description = "INSTAGRAM IMAGE"

admin.site.register(insta_post,instadmin)    


# ============================  ALL-PRODUCT  ==========================
class AllProAdmin(admin.ModelAdmin):
    list_display = ("all_pro_img","product_name","product_price","product_details","allcat","extra_img1_display","extra_img2_display","extra_img3_display","extra_img4_display","extra_img5_display",'add_in_best_seller')
    
    
    def all_pro_img(self,obj):
        return mark_safe("<img src={} height='100px' width='100px' />".format(obj.product_img.url))
    all_pro_img.short_description = "PRODUCT-IMAGES"
    
    def allcat(sself,obj):
        return obj.category_nam.category_name if obj.category_nam else None    
    allcat.short_description = "CATEGORY NAME" 
    
    
    
    def extra_img1_display(self, obj):
        if obj.extra_img1:
            return mark_safe("<img src={} height='80px' width='90px' />".format(obj.extra_img1.url))
        else:
            return "NO IMAGE"    
    extra_img1_display.short_description = 'Extra Image 1'

    def extra_img2_display(self, obj):
        if obj.extra_img2:
            return mark_safe("<img src={} height='80px' width='90px' />".format(obj.extra_img2.url))
        else:
            return "NO IMAGE"    
    extra_img2_display.short_description = 'Extra Image 2'

    def extra_img3_display(self, obj):
        if obj.extra_img3:
            return mark_safe("<img src={} height='80px' width='90px' />".format(obj.extra_img3.url))
        else:
            return "NO IMAGE"        
    extra_img3_display.short_description = 'Extra Image 3'

    def extra_img4_display(self, obj):
        if obj.extra_img4:
            return mark_safe("<img src={} height='80px' width='90px' />".format(obj.extra_img4.url))
        else:
            return "NO IMAGE"     
    extra_img4_display.short_description = 'Extra Image 4'

    def extra_img5_display(self, obj):
        if obj.extra_img5:
            return mark_safe("<img src={} height='80px' width='90px' />".format(obj.extra_img5.url))
        else:
            return "NO IMAGE"    
    extra_img5_display.short_description = 'Extra Image 5'  

admin.site.register(AllProduct,AllProAdmin)

# ============================  ADDRESS  ==========================

class AddressAdmin(admin.ModelAdmin):
    list_display = ("user","fname","lname","phone","address","city","state","zipcode")

admin.site.register(Address,AddressAdmin)

# ============================  CART  ==========================

class CartAdmin(admin.ModelAdmin):
    list_display = ("user","pro","imgofpro","quantity")
    
    def pro(self,obj):
        return f"{obj.product.id} {obj.product.product_name} -Rs.{obj.product.product_price}"
    pro.short_description ="PRODUCT"
    
    def imgofpro(self,obj):
        return mark_safe ("<img src={} height='120px' width='150px' />".format(obj.product.product_img.url))
    imgofpro.short_description = "PRODUCT IMAGE"
    
admin.site.register(Cart,CartAdmin)    





class OrderAdmin(admin.ModelAdmin):
    list_display = ("user","product","product_img_link","quantity","address","order_date","cust")
    
    def product_img(self,obj):
        return mark_safe("<img src={} height='120px' width='140px'/>".format(obj.product.product_img.url))
    
    def product_img_link(self,obj):
        link = reverse("admin:myapp_allproduct_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, self.product_img(obj))

    def cust(self,obj):
        link = reverse("admin:myapp_address_change",args=[obj.address.pk])
        return format_html("<a href='{}' target='_self'> {} </a>",link,obj.address.fname)
    

    
admin.site.register(Order,OrderAdmin)    
     
        
