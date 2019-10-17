from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserCreateSerializer, CurrencyListSerializer,ProfileDetailViewSerializer, MyTokenObtainPairSerializer
from .models import Crypto, Profile


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class CryptoListAPIView(ListAPIView):
    queryset = Crypto.objects.all()
    serializer_class = CurrencyListSerializer


# API view, that will grab the logged in users profile
class ProfileDetailAPIView(APIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailViewSerializer

# create api view that prints whatever is recieving

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer