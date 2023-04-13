from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import View
from django.views.decorators.cache import cache_control


class Login(View):
    return_url = None

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request):
        Login.return_url = request.GET.get ('return_url')
        return render (request, 'login.html')

    def post(self, request):
        email = request.POST.get ('email')
        password = request.POST.get ('password')
        customer = Customer.get_customer_by_email (email)
        
        error_message = None
        if not password:
            error_message = "Please enter your password!"
        
        if not error_message:    
            if customer:
                flag = check_password (password, customer.password)
                if flag:
                    request.session['customer'] = customer.id

                    if Login.return_url:
                        return HttpResponseRedirect (Login.return_url)
                    else:
                        Login.return_url = None
                        if customer.userType == 'buyer':
                            return redirect ('store')
                        elif customer.userType == 'seller':
                            return redirect ('sellerMenu')
                        elif customer.userType == 'admin':
                            pass
                else:
                    error_message = 'Invalid !!'
            else:
                error_message = 'Invalid !!'

        print (email, password)
        return render (request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')
