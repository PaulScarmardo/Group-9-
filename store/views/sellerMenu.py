from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
from store.models.customer import Customer
from store.models.product import Products


class sellerMenu(View):

    def get(self, request):
        customer = request.session.get('customer')
        user = Customer.objects.get(id= customer)
        balance = user.balance
        inventory = Products.objects.filter(seller=user.email)
        
        data = {
            'balance': balance,
            'inventory': inventory
        }
        
        return render (request, 'sellerMenu.html', data)

    def post(self, request):
        return redirect ('addProduct')
