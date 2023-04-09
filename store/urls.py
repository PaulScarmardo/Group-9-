from django.contrib import admin
from django.urls import path
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.sellerMenu import sellerMenu
from .views.addProduct import addProduct
from .views.viewBalance import viewBalance
from .views.find import find
from .views.editProduct import editProduct, delete, saveProduct
from .middlewares.auth import  auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
    path('sellerMenu', sellerMenu.as_view() , name='sellerMenu'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('viewBalance', viewBalance.as_view(), name='viewBalance'),
    path('find', find.as_view(), name='find'),
    path('addProduct', addProduct.as_view() , name='addProduct'),
    path('editProduct', editProduct.as_view(), name='editProduct'),
    path('delete', delete, name='delete'),
    path('saveProduct', saveProduct, name='saveProduct'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]
