from rest_framework import serializers

from order.models import Order

from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)
    products_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        write_only=True,
        many=True
    )
    total = serializers.SerializerMethodField()
    
    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        
        return total
    
    class Meta:
        model = Order
        fields = [
            'product',
            'user',
            'total',
            'products_id'
        ]
        extra_kwargs = {}

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        product_data = validated_data.pop('products_id')
        
        order = Order.objects.create(**validated_data)
        for product in product_data:
            order.product.add(product)
