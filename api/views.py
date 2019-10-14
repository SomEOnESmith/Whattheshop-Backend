from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import UserCreateSerializer, CurrencyListSerializer

from .models import Crypto


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class CryptoListAPIView(ListAPIView):
	queryset = Crypto.objects.all()
	serializer_class = CurrencyListSerializer