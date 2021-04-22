from django.test import TestCase, Client, RequestFactory
from django.contrib.auth import  get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from decimal import Decimal
from .views import recalc_cart, AddToCartView, BaseView
from unittest  import mock
from django.contrib.messages.storage.fallback import FallbackStorage
from .models import Category,CartProduct,Cart,Customer, Product
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

User = get_user_model()

class ShopTestCases(TestCase):
    def  setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='password')
        self.category = Category.objects.create(name='Ноутбуки', slug='notebooks')
        image = SimpleUploadedFile("gsmarena_002-1-2_jpg.", content=b'', content_type='image/jpeg')
        self.product = Product.objects.create(
            category=self.category,
            #brand=self.brand,
            title='test Notebook',
            slug='test-slug',
            image='gsmarena_002-1-2_jpg.',
            price=Decimal('50000.00'),
            description='17.3'


        )
        self.customer = Customer.objects.create(
            user=self.user, phone='112323211', address="Poselkovaya 5633"
        )
        self.cart = Cart.objects.create(owner=self.customer)
        self.cart_product = CartProduct.objects.create(
            user=self.customer,
            cart=self.cart,
            product=self.product

        )
    def test_add_to_cart(self):
        self.cart.products.add(self.cart_product)
        recalc_cart(self.cart)
        self.assertIn(self.cart_product, self.cart.products.all())
        self.assertEqual(self.cart.products.count(), 1 )
        self.assertEqual(self.cart.final_price, Decimal('50000.00'))
    def test_response_from_add_to_cart_view(self):
        factory = RequestFactory()
        request = factory.get('')
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        request.user = self.user
        response= AddToCartView.as_view()(request, ct_model="notebook", slug="test-slug")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/cart/')
    def test_mock_homepage(self):## Тест входа юзера с гл.страницы
        mock_data = mock.Mock(status_code =444)
        with mock.patch('mainapp.views.BaseView.get', return_value = mock_data) as mock_data:
            factory = RequestFactory()
            request = factory.get('')
            request.user = self.user
            response = BaseView.as_view()(request)
            self.assertEqual(response.status_code,444)
            print(mock_data.called)






