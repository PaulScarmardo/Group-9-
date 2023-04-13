from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import Products
from django.views.decorators.cache import cache_control

class Cart(View):
    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self , request):
        if (request.session.get('customer')):
            ids = list(request.session.get('cart').keys())
            products = Products.get_products_by_id(ids)
            print(products)
            return render(request , 'cart.html' , {'products' : products} )
        else:
            return redirect('login')

