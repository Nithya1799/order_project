from django.urls import path
from .views import (
    RegisterView,
    ProductCreateView,
    OrderCreateView,
    MyOrdersView,
    AllOrdersView
)
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    # 🔐 Auth
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),

    # 📦 Product (Admin only)
    path('products/', ProductCreateView.as_view(), name='create-product'),

    # 🛒 Orders (Customer)
    path('orders/', OrderCreateView.as_view(), name='create-order'),
    path('my-orders/', MyOrdersView.as_view(), name='my-orders'),

    # 👑 Admin Orders
    path('all-orders/', AllOrdersView.as_view(), name='all-orders'),
]