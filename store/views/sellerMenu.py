from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
from store.models.customer import Customer
from store.models.product import Products
from django.views.decorators.cache import cache_control


class sellerMenu(View):

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request):
        if (request.session.get('customer')):
            customer = request.session.get('customer')
            user = Customer.objects.get(id= customer)
            balance = user.balance
            inventory = Products.objects.filter(seller=user.email)
            
            data = {
                'balance': balance,
                'inventory': inventory
            }
            
            return render (request, 'sellerMenu.html', data)
        else:
            return redirect('login')

    def post(self, request):
        return redirect ('addProduct')
