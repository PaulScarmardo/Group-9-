from django.test import TestCase
from django.urls import reverse
from store.models.product import Products
from store.models.category import Category
from django.contrib.auth.models import User

class SellerTest(TestCase):
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
                                            image="placeholder",
                                            quantity=1,
                                            seller="user@seller.com")

    def test_add_product_page(self):
        response = self.client.get(reverse('addProduct'))
        self.assertTemplateUsed(response, 'addProduct.html')
    
    def test_edit_product(self):
        response = self.client.post(reverse('editProduct'), data={'item': self.product.id})
        self.assertTemplateUsed(response, 'editProduct.html')
        product = response.context['product']
        self.assertEqual(product, self.product)
        
    def test_product_price_error(self):
         response = self.client.post(reverse('saveProduct'), data={'product': self.product.id, 'price': 0})
         self.assertEqual(response.status_code, 200)
         self.assertContains(response, "The price must be a positive number!")
         
    def test_product_quantity_error(self):
         response = self.client.post(reverse('saveProduct'), data={'product': self.product.id, 'price': 3, 'quantity': -1})
         self.assertEqual(response.status_code, 200)
         self.assertContains(response, "The number of product in stock cannot be a negative number!")

    def test_delete_product(self):
        response = self.client.post(reverse('delete'), data={'item': self.product.id})
        self.assertEqual(str(Products.get_all_products()).strip("<QuerySet "), str([])+">")
        self.assertEqual(response.status_code, 302)

    def test_seller_menu(self):
        response = self.client.post(reverse('sellerMenu'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('addProduct'))

    def test_sign_up_as_seller(self):
        response = self.client.post(reverse('signup'), data={"user_class": "seller"})
        buyer = response.context['values']['userType']
        self.assertEqual(buyer, "seller")