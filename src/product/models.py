import uuid

from django.db import models


def get_default_product_id():
    return '{}'.format(uuid.uuid4())


class Product(models.Model):
    product_id = models.CharField(
        unique=True, max_length=50, default=get_default_product_id,
        help_text='ID generated for products as a reference if product fails')
    category = models.CharField(max_length=50)
    product_name = models.CharField(max_length=99)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return '{brand} {product_name} {category} {price}'.format(
                model_name=self.__class__.__name__,
                brand=self.brand,
                product_name=self.product_name,
                category=self.category,
                price=self.price,
            )
