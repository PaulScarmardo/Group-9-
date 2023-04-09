from django.shortcuts import render , redirect
from store.models.product import Products
from store.models.category import Category
from django.views import View

class find(View):
    
    def post(self, request):
        item = request.POST.get('item')
        categories = Category.get_all_categories()
        
        try:
            items = Products.objects.filter(name__icontains=item)
        except:
            items = None
            
        data = {}
        data['products'] = items
        data['categories'] = categories
        
        return render(request, 'index.html', data)