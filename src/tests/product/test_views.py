from rest_framework.test import APITestCase


# TODO Add integration tests for endpoint
class TestProductDetailView(APITestCase):
    def test_succesful_product_record(self):
        resp = self.client().post('/product/')
