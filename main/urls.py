from django.urls import path
from.views import *

urlpatterns = [
    path('',index_view, name="index"),
    path('about/',about_view, name="about"),
    path('blog-detail/<int:pk>/',blog_detail_view, name="blog-detail"),
    path('blog/',blog_view, name="blog"),
    path('cart/',cart_view, name="cart"),
    path('checkout/',checkout_view, name="checkout"),
    path('compare/',compare_view, name="compare"),
    path('contact/',contact_view, name="contact"),
    path('faq/',faq_view, name="faq"),
    path('login-register',login_register_view, name="login-register"),
    path('register',register_view, name="register"),
    path('logout',logout_view, name="logout"),
    path('my-account/',my_account_view, name="my-account"),
    path('shop/',shop_view, name="shop"),
    path('search/',search_view, name="search"),
    path('product-single/<int:pk>/',product_single_view, name="product-single"),
    path('wishlist/',wishlist_view, name="wishlist"),
    path('card/',cart_view, name="card"),
    
    path('add-wishlist/<int:pk>/',add_wishlist_view, name="add-wishlist"),
    path('remove-wishlist/<int:pk>/',remove_wishlist_view, name="remove-wishlist"),
    path('add-card/<int:pk>/',add_card_view, name="add-card"),
    path('remove-card/<int:pk>/',remove_card_view, name="remove-card"),
]