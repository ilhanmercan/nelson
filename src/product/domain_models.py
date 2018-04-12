from . import models


class ProductDetailDomainModel(object):
    def __init__(self, params):
        self.product_detail_info = params
        self.product_id = self.store_product_detail()

    def store_product_detail(self):
        stored_product = models.Product.objects.create(**self.product_detail_info)
        return stored_product.product_id
