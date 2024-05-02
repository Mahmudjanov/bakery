from django.shortcuts import render, redirect
from.models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def index_view(request):
    card = []
    count = 0
    user = request.user
    if user.is_authenticated:
        card = Card.objects.filter(user=user)
        count = card.count()
    context = {
        'card' : card,
        'count' : count,
        'banner' : Banner.objects.last(), 
        'ad' : Ad.objects.filter(is_full=False).order_by("-id")[:4],
        'ad_full' : Ad.objects.filter(is_full=True).last(),
        'new_product' : Product.objects.all().order_by("-id")[:8],
        'seller_product' : Product.objects.all().order_by("-id")[:8],
        'rated_product' : Product.objects.all().order_by("-rating")[:8],
        'partner' : Partners.objects.all(),
        'testimonial': Testimonial.objects.all(),
        'information' : Information.objects.last(),
        'blog': Blog.objects.all(),
        'product' : Product.objects.all(),
    }
    return render(request, 'index.html', context)

def about_view(request):
    card = []
    user = request.user
    if user.is_authenticated:
        card = Card.objects.filter(user=user)
    context = {
        'card' : card,
        'about' : AboutUs.objects.all().order_by("-id")[:2],
        'partner': Partners.objects.all(),
        'team' : Team.objects.all(),
        'ad' : Ad.objects.filter(is_full=False).order_by("-id")[:4],
    }
    return render(request, "about.html", context)

def blog_detail_view(request, pk):
    card = []
    user = request.user
    if user.is_authenticated:
        card = Card.objects.filter(user=user)
    context = {
        'card' : card,
        'blog':Blog.objects.get(id=pk)
    }
    return render(request, "blog-detail-fullwidth.html", context)

def blog_view(request):
    card = []
    user = request.user
    if user.is_authenticated:
        card = Card.objects.filter(user=user)
    context = {
        'card' : card,
        'blog':Blog.objects.all()
    }
    return render(request, "blog-fullwidth.html.", context)

def cart_view(request):
    card = []
    user = request.user
    if user.is_authenticated:
        card = Card.objects.filter(user=user)
    context = {
        'card' : card,
    }
    return render(request, "cart.html", context)

def checkout_view(request):
    card = []
    user = request.user
    if user.is_authenticated:
        card = Card.objects.filter(user=user)
    context = {
        'card' : card,
    }
    return render(request, "checkout.html", context)

def compare_view(request):

    return render(request, "compare.html")

def contact_view(request):
    card = []
    user = request.user
    if user.is_authenticated:
        card = Card.objects.filter(user=user)
    context = {
        'card' : card,
        'info':Information.objects.last()
    }
    return render(request, "contact.html", context)

def faq_view(request):
    card = []
    user = request.user
    if user.is_authenticated:
        card = Card.objects.filter(user=user)
    context = {
        'card' : card,
        'faq' : Faq.objects.all()
    }
    return render(request, "faq.html", context)

def login_register_view(request):
    if request.method == "POST":
        username = request.POST. get('username')
        password = request.POST.get('password')
        user = User. objects. filter (username=username)
        if user.count() > 0:
           usr = authenticate(username=username, password=password)
           if usr is not None:
               login(request, usr)
               return redirect('index')
        else:
                return redirect('login-register')
    context = {
        'info':Information.objects.last()
    }
    return render(request, "login-register.html", context)
    

def logout_view(request):
    logout(request)
    return redirect('index')


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")
        if password ==confirm:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect("index")
        else:
            return redirect("login-register")


def my_account_view(request):
    return render(request, "my-account.html")

def shop_view(request):
    card = []
    user = request.user
    if user.is_authenticated:
        card = Card.objects.filter(user=user)
    context = {
        'card' : card,
        'product':Product.objects.all().order_by("-id")
    }
    return render(request, "shop-fullwidth.html", context)

def search_view(request):
    q = request.GET.get('q')
    product = Product.objects.filter(name__icontains=q)
    card = []
    user = request.user
    if user.is_authenticated:
        card = Card.objects.filter(user=user)
    context = {
        'card' : card,
        'product':product,
    }
    return render(request, "search.html", context)

def product_single_view(request, pk):
    card = []
    user = request.user
    if user.is_authenticated:
        card = Card.objects.filter(user=user)
    context = {
        'card' : card,
        'product':Product.objects.get(id=pk),
        'similar':Product.objects.filter(category=Product.objects.get(id=pk).category)
    }
    return render(request, "single-product.html", context)

def wishlist_view(request):
    user = request.user
    card = []
    user = request.user
    if user.is_authenticated:
        card = Card.objects.filter(user=user)
    context = {
        'card' : card,
        'product':Wishlist.objects.filter(user=user)
    }
    return render(request, "wishlist.html", context)


def add_wishlist_view(request, pk):
    user = request.user
    Wishlist.objects.create(user=user, product_id=pk)
    return redirect('index')


def remove_wishlist_view(request, pk):
    Wishlist.objects.get(id=pk).delete()  
    return redirect('wishlist')


def cart_view(request):
    user = request.user
    card = []
    user = request.user
    if user.is_authenticated:
        card = Card.objects.filter(user=user)
    context = {
        'card' : card,
        'product':Card.objects.filter(user=user)
    }
    return render(request, "cart.html", context)   


def add_card_view(request, pk):
    user = request.user
    Card.objects.create(user=user, product_id=pk)
    return redirect('index')


def remove_card_view(request, pk):
    Card.objects.get(id=pk).delete()  
    return redirect('card')