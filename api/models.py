from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
 name = models.CharField(max_length=200)
 price = models.DecimalField(max_digits=10, decimal_places=2)
 description = models.TextField(blank=True)
 image = models.URLField(blank=True)


def __str__(self):
 return self.name


class Cart(models.Model):
 user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
 updated_at = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
 cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
 product = models.ForeignKey(Product, on_delete=models.CASCADE)
 quantity = models.PositiveIntegerField(default=1)


class Meta:
 unique_together = ('cart', 'product')


class Order(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 created_at = models.DateTimeField(auto_now_add=True)
 total = models.DecimalField(max_digits=12, decimal_places=2)


class OrderItem(models.Model):
 order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
 product = models.ForeignKey(Product, on_delete=models.CASCADE)
 quantity = models.PositiveIntegerField()
 price = models.DecimalField(max_digits=10, decimal_places=2)
