from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from .serializers import UserCreateSerializer, CurrencyListSerializer,ProfileDetailViewSerializer, UserLoginSerializer

from .models import Crypto, Profile

# login imports
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class CryptoListAPIView(ListAPIView):
    queryset = Crypto.objects.all()
    serializer_class = CurrencyListSerializer

# newwwwwwwwwww

class ProfileDetailAPIView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailViewSerializer


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        my_data = request.data
        serializer = UserLoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)


