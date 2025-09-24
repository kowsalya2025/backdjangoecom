from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Cart, CartItem, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
 class Meta:
  model = Product
  fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
 product = ProductSerializer(read_only=True)
 product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)


class Meta:
 model = CartItem
 fields = ['id', 'product', 'product_id', 'quantity']


class CartSerializer(serializers.ModelSerializer):
 items = CartItemSerializer(many=True)


class Meta:
 model = Cart
 fields = ['id', 'user', 'items']
 read_only_fields = ['user']


class OrderItemSerializer(serializers.ModelSerializer):
 product = ProductSerializer(read_only=True)
class Meta:
 model = OrderItem
 fields = ['product', 'quantity', 'price']


class OrderSerializer(serializers.ModelSerializer):
 items = OrderItemSerializer(many=True)
class Meta:
 model = Order
 fields = ['id', 'user', 'created_at', 'total', 'items']
 read_only_fields = ['user', 'created_at']


class UserSerializer(serializers.ModelSerializer):
 password = serializers.CharField(write_only=True)
class Meta:
 model = User
 fields = ('id', 'username', 'email', 'password')


def create(self, validated_data):
  user = User(username=validated_data['username'], email=validated_data.get('email',''))
  user.set_password(validated_data['password'])
  user.save()
# create empty cart
  Cart.objects.create(user=user)
  return user