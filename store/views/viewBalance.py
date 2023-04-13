from django.shortcuts import render , redirect
from django.views import View
from store.models.customer import Customer
from django.views.decorators.cache import cache_control

class viewBalance(View):

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request):
        if (request.session.get('customer')):
            balance = Customer.objects.get(id= request.session.get('customer')).balance
            return render (request, 'viewBalance.html', {'balance': balance})
        else:
            return redirect('login')

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def post(self, request):
        if (request.session.get('customer')):
            postData = request.POST
            amount = postData.get('amount')
            buyer = Customer.objects.get(id= request.session.get('customer'))
            
            error_message = None
            error_message = self.validateAmount (amount)
            
            if not error_message:
                buyer.balance += int(amount)
                buyer.save() 
            else:
                balance = Customer.objects.get(id= request.session.get('customer')).balance
                return render (request, 'viewBalance.html', {'error': error_message, 'balance': balance})     
            
            return redirect ('viewBalance')
        else:
            return redirect('login')
        
    def validateAmount(self, amount):
        error_message = None
        if int(amount) < 1:
            error_message = "The amount must be positive!"
        # saving

        return error_message