from django.test import TestCase, Client
from django.urls import reverse
from store.models.product import Products
from store.models.category import Category
from store.models.customer import Customer
from store.models.orders import Order
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class BuyerTest(TestCase):
    def setUp(self):
        User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
        self.client.login(username='admin', password='admin')
        session = self.client.session
        session['customer'] = 123
        session.save()
        self.category = Category.objects.create(name="testItems")
        self.product = Products.objects.create(name="item1",
                                            price=100,
                                            category=Category.objects.get(name= self.category),
                                            description="test item 1",
                                            quantity=1,
                                            image="placeholder",
                                            seller="user@seller.com")
        self.customer = Customer.objects.create(first_name="firstName",
                                                last_name="lastName",
                                                phone="1234567890",
                                                email="user@test.com",
                                                password=make_password ("pass"),
                                                userType="buyer",
                                                balance=100,
                                                id=session['customer'])
        
    def test_search(self):
        response = self.client.post(reverse('find'), data={'item': "NonexistentItem"})
        items = response.context['products']
        self.assertEqual(len(items), 0)
        
    def test_add_to_cart(self):
        response = self.client.post(reverse('homepage'), data={'product': self.product, 'remove': False})
        self.assertEqual(self.client.session.get('cart')[str(self.product).split(':')[-1].strip()], 1)   
    
    def test_browse_category(self):
        response = self.client.get(reverse('store'), data={'category': self.category.id})
        products = response.context['products']
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0], self.product)
        
    def test_display_products(self):
        response = self.client.get(reverse('store'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        
    def test_return_product(self):
        self.seller = Customer.objects.create(first_name="firstName",
                                                last_name="lastName",
                                                phone="1234567890",
                                                email="user@seller.com",
                                                password=make_password ("pass"),
                                                userType="seller",
                                                balance=0)
        self.order = Order.objects.create(customer=Customer(id=self.customer.id),
                                            product=self.product,
                                            price=self.product.price,
                                            address="",
                                            phone="",
                                            quantity=1,
                                            seller="user@seller.com")
        response = self.client.post(reverse('orders'), data={'order': self.order.id})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('orders'))
        
    def test_sign_up_as_buyer(self):
        response = self.client.post(reverse('signup'), data={"user_class": "buyer"})
        buyer = response.context['values']['userType']
        self.assertEqual(buyer, "buyer")