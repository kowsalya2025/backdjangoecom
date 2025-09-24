from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CartAPIView, CheckoutAPIView, RegisterAPIView, LoginAPIView

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('cart/', CartAPIView.as_view(), name='cart'),
    path('checkout/', CheckoutAPIView.as_view(), name='checkout'),
    path('auth/register/', RegisterAPIView.as_view(), name='register'),
    path('auth/login/', LoginAPIView.as_view(), name='login'),
]
