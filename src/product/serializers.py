from rest_framework import serializers


class ProductDetailInputSerializer(serializers.Serializer):
    category = serializers.CharField()
    product_name = serializers.CharField()
    brand = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)


class ProductDetailOutputSerializer(serializers.Serializer):
    product_id = serializers.CharField()
