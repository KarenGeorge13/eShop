from rest_framework import serializers
from market.models import Product, ProductType, Player, Game, Cart, Order
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    product_type = serializers.PrimaryKeyRelatedField(many=False, queryset=ProductType.objects.all())

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'product_image', 'manufacturer', 'release_date', 'product_type']


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['id', 'name', 'description']


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'name', 'description']


class PlayerSerializer(serializers.ModelSerializer):
    game = serializers.PrimaryKeyRelatedField(many=False, queryset=Game.objects.all())
    devices = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = Player
        fields = ['id', 'game', 'devices']


class CartSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = Cart
        fields = ['id', 'products', 'price']


class OrderSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = Order
        fields = ['id', 'products', 'price']

