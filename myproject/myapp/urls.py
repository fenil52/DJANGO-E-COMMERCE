from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    
    path("productview/<slug:slug>",productview,name="productview"),
    path("all_product/<cat_name>",allproduct,name="all_product"),
    path("all_product/",allproduct,name="all_product"),


    path("login_page/",login_page,name="login_page"),
    

    path("plus/",plus_cart,name="plus"),
    path('minus/',minus_cart, name='minus'),
    path('remove_cart/',remove_cart, name='remove_cart'),

    path("reg_page/",reg_page,name="reg_page"),
    
    path("log_out/",log_out,name="log_out"),
    
    path("orders/",orders,name="orders"),

    path("save_check_addr/",save_check_addr,name="save_check_addr"),

    path("profile/",profile,name="profile"),
    
    path("addresse/",address,name="address"),
    path('edit_address/<int:addrid>/', address_edit, name='edit_address'),
    
    path('delete/<int:address_id>/',delete_address, name='delete_address'),
    
    path("cart/",cart,name="cart"),
    path("save_cart/",save_cart,name="save_cart"),
    path("checkout/",checkout,name="checkout"),
    
]
