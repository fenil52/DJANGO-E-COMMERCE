from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib import messages
from django.core.mail import send_mail
from myproject.settings import EMAIL_HOST_USER
from django.utils.html import strip_tags
from django.contrib.auth.decorators import login_required 

from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.http import JsonResponse
from .models import *

from django.shortcuts import render
from django.db.models import Q
from .models import AllProduct

def home(request):
    if request.user.is_authenticated:
         user=request.user
         totalnumber = len(Cart.objects.filter(user=user))
    else:
        totalnumber = 0    
    bestseller=AllProduct.objects.filter(add_in_best_seller=True)
    main_slider = Mainslider.objects.all()
    cat =Category.objects.all()
    onemonth=ProductMonth.objects.get()
    email_bg_img = emailbg.objects.get()
    insta_im=insta_post.objects.all()
    
   
    context = {
        'main_slider':main_slider,
        'cat':cat,
        'onemonth':onemonth,
        'email_bg_img':email_bg_img,
        'insta_im':insta_im,
        'bestseller':bestseller,
        'totalnumber':totalnumber
    }
    return render(request,"index.html",context)


def login_page(request):
    if request.method == "POST":
        us = request.POST.get("mail")
        password = request.POST.get("password")
        
        fin = authenticate(request,username=us,password=password)
        
        if fin is not None:
            login(request,fin)
            return redirect("/profile")
        else:
            messages.info(request,"Username or Password Incorrect :)")
            return redirect("/login_page")
                
    return render(request,"login_page.html")   


def reg_page(request):
    if request.method == "POST":
        
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        mail=request.POST.get("mail")
        pa=request.POST.get("pass")
        
        fe = User.objects.filter(email=mail).exists()
        
        if fe:
            messages.error(request, 'Your Email Is Already Registered')
            return redirect("/reg_page")
        fin = User(
            first_name=fname,
            last_name=lname,
            email=mail,
            username=mail
        )
        
        subject = "	Customer account confirmation"
        html_message = '''
        <html>
        <body>
    
    <h1 style="font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; font-weight: normal; font-size: 24px; padding: 10px;">RESIN PROFESSIONAL </h1>
    
    <h2 style="font-family:Arial, Helvetica, sans-serif; font-size: 22px; letter-spacing: 1px; font-weight: normal;padding: 20px 10px; ">Welcome to RESIN PROFESSIONAL!</h2>

    <p style=" padding-left: 10px; font-family: Arial, Helvetica, sans-serif; color: grey; width: 70%;">You've activated your customer account. Next time you shop with us, log in for faster checkout.</p>

    <button style="margin-top: 10px; margin-left: 10px; margin-bottom: 20px;border: none; padding: 19px; border-radius: 5px; background-color: rgb(52, 144, 169); font-family:Verdana, Geneva, Tahoma, sans-serif; letter-spacing: 1px;">
    <a href="/" style="text-decoration: none; background-color: rgb(52, 144, 169); color:#fff;">VISIT OUR STORE</a></button>

    <hr style="color: rgba(94, 87, 87,0.2);">
    <p style="text-align: center; color: rgba(88, 98, 107,0.7) ; font-family: Arial, Helvetica, sans-serif; font-size: 15px;padding: 5px;">
        If you have any questions, reply to this email or contact us at resinprofessional@gmail.com
    </p>
</body>
        </html>
        '''
        
        send_mail (
            subject,
            strip_tags(html_message),
            EMAIL_HOST_USER,
            [mail],
            fail_silently=True,
            html_message=html_message
        )
        fin.set_password(pa)
        fin.save()
        messages.success(request, 'Your Registered Successfully :)')
    
    return render(request,"register_page.html")   

def log_out(request):
    logout(request)
    return redirect("/")

@login_required(login_url="/login_page")
def profile(request):
    if request.user.is_authenticated:
        totalnumber = len(Cart.objects.filter(user=request.user))
        order=Order.objects.filter(user=request.user)
        con = {
            'totalnumber':totalnumber,
            'order':order
        }
    else:
        totalnumber= 0    
    return render(request,"profile.html",con)


'''
fname
lname
phone
address
city
state
zipcode
'''
@login_required(login_url="/login_page")
def address(request):
    
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        

        fin = Address(
            fname=fname,
            lname=lname,
            phone=phone,
            address=address,
            city=city,
            state=state,
            zipcode=zipcode,
            user=request.user
        )
        fin.save()
        messages.success(request, 'Address Added Successfully :)')
        return redirect("/addresse/")
    if request.user.is_authenticated:
        us = request.user
        totalnumber = len(Cart.objects.filter(user=us))
        address_items = Address.objects.filter(user=request.user)
        context = {
            'us': us,
            'address': address_items,
            'totalnumber':totalnumber
        }
        return render(request, "edit-address.html", context)

    return render(request, "edit-address.html")

      
      
def address_edit(request, addrid):
    address_instance = Address.objects.get(id=addrid)

    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')

        # Update the existing Address instance with the new data
        address_instance.fname = fname
        address_instance.lname = lname
        address_instance.phone = phone
        address_instance.address = address
        address_instance.city = city
        address_instance.state = state
        address_instance.zipcode = zipcode

        # Save the updated instance
        address_instance.save()

        return redirect('/addresse')

    return render(request, 'edit-address.html', {'address_instance': address_instance})



from django.shortcuts import get_object_or_404

def delete_address(request, address_id):
    address_instance = get_object_or_404(Address, id=address_id)
    address_instance.delete()
    messages.success(request, 'Address deleted successfully.')
    return redirect("/addresse/")
    

def save_cart(request):
    if request.user.is_authenticated:
        user = request.user
        product = request.GET.get("prod_id")
        main =AllProduct.objects.get(slug=product)
        save_data,boo = Cart.objects.get_or_create(user=user,product=main)
        if not boo:
            return redirect("/cart")
        save_data.save()
        return redirect("/cart") 
    else:
        messages.info(request,"Please Login ...")   
        return redirect("/login_page")
    
    
    
def save_check_addr(request):
     if request.method == "POST" and request.user.is_authenticated:
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        address =request.POST.get('address')
        city = request.POST.get('city')
        zipcode = request.POST.get('zipcode')
        state = request.POST.get('state')
        phone = request.POST.get('phone')
        user=request.user
        
        fi = Address(
            fname=fname,
            lname=lname,
            address=address,
            city=city,
            state=state,
            phone=phone,
            zipcode=zipcode,
            user=user
        )
        fi.save()
        return redirect("/checkout")    
    
import uuid
import random
import string

def checkout(request):
    if request.user.is_authenticated:
        user = request.user
        totalnumber = len(Cart.objects.filter(user=user))
        cart = Cart.objects.filter(user=user)
        addr = Address.objects.filter(user=user)
        
        amount = 0
        shipping = 50
        
        for item in cart:
            subtotal = item.quantity * item.product.product_price
            item.subtotal = subtotal
            amount += subtotal
        
        shipping += amount
        total = shipping
        total_amount_in_paise = total * 100
        
    else:
        totalnumber = 0  
        return redirect("/login_page")
        
    con = {
        'totalnumber': totalnumber,
        'cart': cart,
        'addr': addr,
        'total': total,
        'total_amount_in_paise':total_amount_in_paise
    }  
        
    return render(request, "checkout.html", con)
      

import random

def productview(request,slug):
    in_already_cart=False
    if request.user.is_authenticated:
        totalnumber = len(Cart.objects.filter(user=request.user))
    else:
        totalnumber = 0    
    all_pro_view = AllProduct.objects.get(slug=slug)
    all_products_except_main = AllProduct.objects.exclude(slug=slug)
    if request.user.is_authenticated:
        totalnumber = len(Cart.objects.filter(user=request.user))
        in_already_cart = Cart.objects.filter(Q(user=request.user) & Q(product =all_pro_view)).exists()
    user=request.user
  
    random_products = random.sample(list(all_products_except_main), min(6, all_products_except_main.count()))

    context = {
        'best_pro_view': all_pro_view,
        'random_products': random_products,
        'totalnumber':totalnumber,
        'in_already_cart':in_already_cart
    }
    return render(request,"ProductView.html",context)


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import AllProduct, Category

from django.db.models import Q

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def allproduct(request):
    if request.user.is_authenticated:
        user = request.user
        totalnumber = Cart.objects.filter(user=user).count()
    else:
        totalnumber = 0

    all_data = AllProduct.objects.all()  # Default queryset
    
    if request.method == "GET":
        query = request.GET.get("search")
        if query:
            # Filter products based on product name containing the query
            all_data = AllProduct.objects.filter(product_name__icontains=query)

    # Pagination
    items_per_page = 16
    paginator = Paginator(all_data, items_per_page)
    page_number = request.GET.get('page', 1)
    try:
        category_filter = paginator.page(page_number)
    except PageNotAnInteger:
        category_filter = paginator.page(1)
    except EmptyPage:
        category_filter = paginator.page(paginator.num_pages)

    # Get random products
    random_products = AllProduct.objects.order_by('?')[:5]

    context = {
        'category_filter': category_filter,
        'random_products': random_products,
        'totalnumber': totalnumber
    }
    return render(request, "all-products.html", context)


def random_products_slider(request):
    user=request.user
    totalnumber = len(Cart.objects.filter(user=user))
    random_products = AllProduct.objects.all().order_by('?')[:5]  # Fetching 5 random products
    context = {'random_products': random_products,'totalnumber':totalnumber}
    return render(request, 'all-products.html', context)

def cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)

        totalnumber = len(cart)

        amount = 0
        shipping = 50
        for item in cart:
            subtotal = item.quantity * item.product.product_price
            item.subtotal = subtotal 
    

        for item in cart:
            temp = item.quantity * item.product.product_price
            amount += temp   
        total = amount + shipping 

        context = {
            'cart': cart,
            'amount': amount,
            'total': total,
            'totalnumber': totalnumber,
        }
        return render(request, "cart.html", context)
    return render(request, "cart.html")





from django.http import JsonResponse
from django.db.models import Q
from .models import Cart

from django.http import JsonResponse
from django.db.models import Q
from .models import Cart

def plus_cart(request):
    if request.method == "GET":      
       pr_i = request.GET["prod_id"]
       cc = Cart.objects.get(Q(product=pr_i) & Q(user=request.user))
       cc.quantity += 1
       cc.save()
       
       subtotal = cc.quantity * cc.product.product_price


       total_amount = sum(item.quantity * item.product.product_price for item in Cart.objects.filter(user=request.user))

       total = total_amount + 50
       
       con = {
           'quantity': cc.quantity,
           'subtotal': subtotal,
           'total': total
       }  
       
       return JsonResponse(con) 
   
   

def minus_cart(request):
    if request.method == "GET":
        pr_i = request.GET.get("prod_id")
        cc = Cart.objects.get(Q(product=pr_i) & Q(user=request.user))
        if cc.quantity > 1:
            cc.quantity -= 1
            cc.save()

        subtotal = cc.quantity * cc.product.product_price
        total_amount = sum(item.quantity * item.product.product_price for item in Cart.objects.filter(user=request.user))
        total = total_amount + 50

        con = {
            'quantity': cc.quantity,
            'subtotal': subtotal,
            'total': total
        }

        return JsonResponse(con)

def remove_cart(request):
    if request.method == "POST":
        pr_i = request.POST.get("prod_id")
        Cart.objects.filter(Q(product=pr_i) & Q(user=request.user)).delete()

        total_amount = sum(item.quantity * item.product.product_price for item in Cart.objects.filter(user=request.user))
        total = total_amount + 50

        con = {
            'total': total
        }

        return redirect("/cart")




from django.shortcuts import get_object_or_404

def orders(request):
    if request.method == "POST" and request.user.is_authenticated:
        # Fetch the selected address
        addr_id = request.POST.get("custid")
        address = get_object_or_404(Address, id=addr_id, user=request.user)
        
        # Retrieve the cart items
        cart = Cart.objects.filter(user=request.user)

        # Create orders for each cart item
        for c in cart:
            order = Order(user=request.user, address=address, quantity=c.quantity, product=c.product)
            order.save()
            c.delete()
                
        # Check if payment was successful
        payment_id = request.POST.get('razorpay_payment_id')
        print("--------------------------",payment_id)
        if payment_id:
            messages.success(request, "Thank you for shopping with us. Your order is confirmed!")

        return redirect("/profile")  # Redirect to the user's profile page

    else:
        return redirect("/profile")  # Redirect if request method is not POST or user is not authenticated
