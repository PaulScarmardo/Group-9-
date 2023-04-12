from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.orders import Order
from store.middlewares.auth import auth_middleware

class OrderView(View):


    def get(self , request ):
        customer = request.session.get('customer')
        user = Customer.objects.get(id= customer)
        if (user.userType == 'buyer'):
            orders = Order.get_orders_by_customer(customer)
            print(orders)
            return render(request , 'orders.html'  , {'orders' : orders})
        elif (user.userType == 'seller'):
            orders = Order.objects.filter(seller=user.email).order_by('-date')
            return render(request , 'sellerOrder.html'  , {'orders' : orders})
        elif (user.userType == 'admin'):
            pass
    
    def post(self, request):
        order = request.POST.get('order')
        prod = Order.objects.get(id=order)
        buyer = Customer.objects.get(id= request.session.get('customer'))
        seller = Customer.get_customer_by_email(prod.product.seller)
        
        prod.product.quantity += prod.quantity
        prod.product.save()
        buyer.balance += (prod.price * prod.quantity)
        buyer.save()
        seller.balance -= (prod.price * prod.quantity)
        seller.save()
        
        prod.delete()
        
        return redirect('orders')