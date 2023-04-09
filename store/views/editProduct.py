from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Products
from store.models.category import Category

class editProduct(View):
    
    def post(self, request):
        product = request.POST.get('item')
        item = Products.objects.get(id=product)
        return render (request, 'editProduct.html', {'product': item})
    
    
def saveProduct(request):
    postData = request.POST
    product = Products.objects.get(id=postData.get('product'))
    name = postData.get ('name')
    price = postData.get ('price')
    category = postData.get ('category')
    description = postData.get ('description')
    image = postData.get('image')
    
    error_message = None
    if int(price) < 1:
        error_message = "The price must be a positive number!"
        
    if not error_message:
        product.name = name
        product.price = price
        product.category = Category.objects.get(name= category)
        product.description = description
        if image != "":
            product.image = "uploads/products/"+image
        product.save()
        return redirect ('sellerMenu')
    else:
        return render (request, 'editProduct.html', {'error': error_message, 'product': product})


def delete(request):
    product = request.POST.get('item')
    item = Products.objects.get(id=product)
    item.delete()
        
    return redirect('sellerMenu')