from django.urls import path

from .views import UserCreateAPIView, CryptoListAPIView, ProfileDetailAPIView

from rest_framework_simplejwt.views import TokenObtainPairView



urlpatterns = [
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('list/', CryptoListAPIView.as_view(), name='list'),
    path('profile/', ProfileDetailAPIView.as_view(), name='api-profile-detail'),
]