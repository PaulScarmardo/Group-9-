from django.test import TestCase 
from django.urls import reverse
from store.models.customer import Customer
from store.models.product import Products
from store.models.category import Category
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class AdminTest(TestCase):
    def setUp(self):
        User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
        self.client.login(username='admin', password='admin')
        session = self.client.session
        session['customer'] = 123
        session.save()
        self.email = "user@test.com"
        self.password = "testPassword"
        
        self.customer = Customer (first_name="firstName",
                             last_name="lastName",
                             phone="1234567890",
                             email=self.email,
                             password=make_password (self.password),
                             userType="buyer",
                             balance=0,
                             status=1)
        self.customer.register()

    def test_return_from_admin(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        
    def test_suspension_page(self):
        response = self.client.get(reverse('accountError'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accountError.html')
    
    def test_buyer_suspension(self):
        self.customer.status = 0
        self.customer.save()
        response = self.client.post(reverse('login'), data={
            'email': self.email,
            'password': self.password,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('accountError'))
        
    def test_seller_suspension(self):
        self.customer.status = 0
        self.customer.userType = "seller"
        self.customer.save()
        response = self.client.post(reverse('login'), data={
            'email': self.email,
            'password': self.password,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('accountError'))
        
    def test_account_unsuspension(self):
        self.customer.status = 1
        self.customer.save()
        response = self.client.post(reverse('login'), data={
            'email': self.email,
            'password': self.password,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('store'))
        
    def test_block_product(self):
        self.category = Category.objects.create(name="testItems")
        self.product = Products.objects.create(name="item1",
                                            price=100,
                                            category=Category.objects.get(name= self.category),
                                            description="test item 1",
                                            image="placeholder",
                                            quantity=1,
                                            seller="user@seller.com")
        self.product.delete()
        self.assertEqual(str(Products.get_all_products()).strip("<QuerySet "), str([])+">")