from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import User, Product, Order
from .serializers import UserSerializer, ProductSerializer, OrderSerializer
from .permissions import IsAdmin, IsCustomer


# 🔐 Register (Customer/Admin)
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# 📦 Admin → Create Product
class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


# 🛒 Customer → Create Order (Nested)
class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsCustomer]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# 👤 Customer → View Own Orders
class MyOrdersView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsCustomer]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


# 👑 Admin → View All Orders
class AllOrdersView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsAdmin]