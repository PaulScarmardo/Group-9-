from django.shortcuts import render , redirect
from store.models.product import Products
from store.models.category import Category
from django.views import View
from django.views.decorators.cache import cache_control

class find(View):
    
    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def post(self, request):
        if (request.session.get('customer')):
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
        else:
            return redirect('login')