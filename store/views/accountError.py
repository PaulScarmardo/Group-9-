from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
from django.views.decorators.cache import cache_control

class accountError(View):
    
    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request):
        if (request.session.get('customer')):
            request.session.clear()
            return render (request, 'accountError.html')
        else:
            return redirect('login')
    
    def post(self, request):
        return redirect ('login')