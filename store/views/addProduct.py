from django.shortcuts import render, redirect
from django.views import View
from store.models.customer import Customer
from store.models.product import Products
from store.models.category import Category
from django.views.decorators.cache import cache_control

class addProduct(View):
    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request):
        if (request.session.get('customer')):
            return render (request, 'addProduct.html')
        else:
            return redirect('login')

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def post(self, request):
        if (request.session.get('customer')):
            postData = request.POST
            name = postData.get ('name')
            price = postData.get ('price')
            category = postData.get ('category')
            seller = Customer.objects.get(id= request.session.get('customer')).email
            description = postData.get ('description')
            quantity = postData.get('quantity')
            image = postData.get('image')
            # validation
            value = {
                'name': name,
                'price': price,
                'category': category,
                'description': description,
                'quantity': quantity,
                'image': image,
                'seller': seller
            }
            error_message = None

            product = Products (name=name,
                                price=price,
                                category=Category.objects.get(name= category),
                                description=description,
                                quantity=quantity,
                                image="uploads/products/"+image,
                                seller=seller)
            error_message = self.validateProduct (product)

            if not error_message:
                product.register ()
                return redirect ('sellerMenu')
            else:
                data = {
                    'error': error_message,
                    'values': value
                }
                return render (request, 'addProduct.html', data)
        else:
            return redirect('login')

    def validateProduct(self, product):
        error_message = None
        if (not product.name):
            error_message = "Please enter your product's name!!"
        elif int(product.price) < 1:
            error_message = "The price must be a positive number!"
        elif int(product.quantity) < 1:
            error_message = "You must have at least 1 item in stock before registering your product!"
        elif not product.image:
            error_message = "Please provide an image of your product"
        # saving

        return error_message