from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Products
from store.models.category import Category
from django.views.decorators.cache import cache_control

class editProduct(View):
    
    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def post(self, request):
        if (request.session.get('customer')):
            product = request.POST.get('item')
            item = Products.objects.get(id=product)
            return render (request, 'editProduct.html', {'product': item})
        else:
            return redirect('login')
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def saveProduct(request):
    if (request.session.get('customer')):
        postData = request.POST
        product = Products.objects.get(id=postData.get('product'))
        name = postData.get ('name')
        price = postData.get ('price')
        category = postData.get ('category')
        description = postData.get ('description')
        quantity = postData.get('quantity')
        image = postData.get('image')
        
        error_message = None
        if int(price) < 1:
            error_message = "The price must be a positive number!"
        elif int(quantity) < 0:
            error_message = "The number of product in stock cannot be a negative number!"
            
        if not error_message:
            product.name = name
            product.price = price
            product.category = Category.objects.get(name= category)
            product.description = description
            product.quantity = quantity
            if image != "":
                product.image = "uploads/products/"+image
            product.save()
            return redirect ('sellerMenu')
        else:
            return render (request, 'editProduct.html', {'error': error_message, 'product': product})
    else:
        return redirect('login')


def delete(request):
    product = request.POST.get('item')
    item = Products.objects.get(id=product)
    item.delete()
        
    return redirect('sellerMenu')