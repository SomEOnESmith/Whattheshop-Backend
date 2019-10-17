from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import UserCreateAPIView, CryptoListAPIView, ProfileDetailAPIView, MyTokenObtainPairView

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('list/', CryptoListAPIView.as_view(), name='list'),
    path('profile/', ProfileDetailAPIView.as_view(), name='api-profile-detail'),
]