from django.test import TestCase 
from django.urls import reverse
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password

class LoginTest(TestCase):
    def setUp(self):
        self.email = "user@test.com"
        self.password = "testPassword"
        
        customer = Customer (first_name="firstName",
                             last_name="lastName",
                             phone="1234567890",
                             email=self.email,
                             password=make_password (self.password),
                             userType="buyer",
                             balance=0)
        customer.register()

    def test_login_view_loads_correctly(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_buyer(self):
        response = self.client.post(reverse('login'), data={
            'email': self.email,
            'password': self.password,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('store'))
        
    def test_login_seller(self):
        customer = Customer.get_customer_by_email(self.email)
        customer.userType = "seller"
        customer.save()
        response = self.client.post(reverse('login'), data={
            'email': self.email,
            'password': self.password,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('sellerMenu'))

    def test_login_wrong_password(self):
        response = self.client.post(reverse('login'), data={
            'username': self.email,
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid !!', html=True)
    
    def test_login_without_password(self):
        response = self.client.post(reverse('login'), data={
            'username': self.email,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please enter your password!", html=True)

    def test_logout(self):
        response = self.client.post(reverse('logout'))
        self.assertEqual(self.client.session.get('_auth_user_id'), None)
        self.assertRedirects(response, reverse('login'))
