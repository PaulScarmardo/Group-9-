from django.shortcuts import render, redirect
from django.views import View
from store.models.customer import Customer
from store.models.product import Products
from store.models.category import Category

class addProduct(View):
    def get(self, request):
        return render (request, 'addProduct.html')

    def post(self, request):
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