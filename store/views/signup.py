from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup (View):
    def get(self, request):
        return render (request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get ('firstname')
        last_name = postData.get ('lastname')
        phone = postData.get ('phone')
        email = postData.get ('email')
        password = postData.get ('password')
        userType = postData.get('user_class')
        balance = 0
        status = 1
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
            'userType': userType,
            'balance': balance,
            'status': status
        }
        error_message = None

        customer = Customer (first_name=first_name,
                             last_name=last_name,
                             phone=phone,
                             email=email,
                             password=password,
                             userType=userType,
                             balance=balance,
                             status=status)
        error_message = self.validateCustomer (customer)

        if not error_message:
            print (first_name, last_name, phone, email, password)
            customer.password = make_password (customer.password)
            customer.register ()
            return redirect ('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render (request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = "Please Enter your First Name !!"
        elif len (customer.first_name) < 2:
            error_message = 'First Name must be 2 char long or more'
        elif not customer.first_name.isalpha():
            error_message = 'First Name must contain only characters'
        elif not customer.last_name:
            error_message = 'Please Enter your Last Name'
        elif len (customer.last_name) < 2:
            error_message = 'Last Name must be 2 char long or more'
        elif not customer.last_name.isalpha():
            error_message = 'Last Name must contain only characters'
        elif not customer.phone:
            error_message = 'Enter your Phone Number'
        elif len (customer.password) < 5:
            error_message = 'Password must be 5 char long'
        elif len (customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists ():
            error_message = 'This Email address has already been registered'
        # saving
        elif not customer.userType:
            error_message = 'Please select the type of user you are registering as'

        return error_message
