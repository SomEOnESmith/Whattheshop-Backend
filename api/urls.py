from django.urls import path

from .views import UserCreateAPIView, CryptoListAPIView, ProfileDetailAPIView, MyTokenObtainPairView, CheckoutCart

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('list/', CryptoListAPIView.as_view(), name='list'),
    path('profile/', ProfileDetailAPIView.as_view(), name='api-profile-detail'),
    path('checkout/', CheckoutCart.as_view(), name='checkout'),
]