from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Products
from store.models.orders import Order


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        
        total = 0
        for product in products:
            total += (product.price * cart.get(str(product.id)))
        
        error_message = None
        if total > Customer.objects.get(id= request.session.get('customer')).balance:
            error_message = "Not enough balance. Please update your balance before checking out."
            
        if not error_message:
            print(address, phone, customer, cart, products)

            for product in products:
                print(cart.get(str(product.id)))
                order = Order(customer=Customer(id=customer),
                            product=product,
                            price=product.price,
                            address=address,
                            phone=phone,
                            quantity=cart.get(str(product.id)),
                            seller=product.seller)
                order.save()
                buyer = Customer.objects.get(id= request.session.get('customer'))
                buyer.balance -= (product.price * cart.get(str(product.id)))
                buyer.save()
                seller = Customer.get_customer_by_email(product.seller)
                seller.balance += (product.price * cart.get(str(product.id)))
                seller.save()
            request.session['cart'] = {}

            return redirect('cart')
        else:
            data = {
                'error': error_message
            }
            return render (request, 'cart.html', data)