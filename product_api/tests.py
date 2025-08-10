from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Product

class ProductAPITests(APITestCase):
    def setUp(self):
        self.product1 = Product.objects.create(
            name="A",
            description="qwertyuiop",
            price=2000.00
        )
        self.product2 = Product.objects.create(
            name="B",
            description="asdfghjkl",
            price=700.01
        )
        self.product3 = Product.objects.create(
            name="C",
            description="ZXCVBNM",
            price=3000.00
        )

    def test_view_products(self):
        url = reverse('product-list')
        resp = self.client.get(url)
        assert resp.status_code == 200
        assert len(resp.data.get('results', resp.data)) >= 3

    def test_filter_products_by_min_price(self):
        url = reverse('product-list') + '?min_price=2000'
        resp = self.client.get(url)
        assert resp.status_code == 200
        for prod in resp.data.get('results', resp.data):
            assert float(prod['price']) >= 2000

    def test_filter_products_by_max_price(self):
        url = reverse('product-list') + '?max_price=2000'
        resp = self.client.get(url)
        assert resp.status_code == 200
        for prod in resp.data.get('results', resp.data):
            assert float(prod['price']) <= 2000

    def test_filter_products_by_name(self):
        url = reverse('product-list') + '?param=A'
        resp = self.client.get(url)
        assert resp.status_code == 200
        found = False
        for prod in resp.data.get('results', resp.data):
            if 'a' in prod['name'].lower():
                found = True
        assert found

    def test_create_product(self):
        url = reverse('product-create')
        data = {
            "name": "D",
            "description": "WASDE",
            "price": 90000.00
        }
        resp = self.client.post(url, data, format='json')
        assert resp.status_code == 201
        assert resp.data['name'] == "D"

    def test_get_product_by_id(self):
        url = reverse('product-detail', args=[self.product2.id])
        resp = self.client.get(url)
        assert resp.status_code == 200
        assert resp.data['id'] == self.product2.id

    def test_update_product(self):
        url = reverse('product-update', args=[self.product1.id])
        data = {
            "name": "E",
            "description": "poiuytrewq",
            "price": 4000.00
        }
        resp = self.client.put(url, data, format='json')
        assert resp.status_code == 200
        assert resp.data['name'] == "E"

    def test_delete_product(self):
        url = reverse('product-delete', args=[self.product3.id])
        resp = self.client.delete(url)
        assert resp.status_code == 204
        assert not Product.objects.filter(id=self.product3.id).exists()
