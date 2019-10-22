from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserCreateSerializer, CurrencyListSerializer,ProfileDetailViewSerializer, MyTokenObtainPairSerializer, ItemTransactionSerializer, TransactionDetailSerializer
from .models import Crypto, Profile, Transaction, TransactionItem


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class CryptoListAPIView(ListAPIView):
    queryset = Crypto.objects.all()
    serializer_class = CurrencyListSerializer


class ProfileDetailAPIView(APIView):
    serializer_class = ProfileDetailViewSerializer
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        profile_serializer = ProfileDetailViewSerializer(request.user.profile)
        return Response(profile_serializer.data, status=HTTP_200_OK)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CheckoutCart(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        profile = request.user.profile
        transaction = Transaction.objects.create(profile=profile)
        try:
            for item_transaction in request.data:
                item_transaction["quantity"] = float(item_transaction["quantity"])
                transaction_item = TransactionItem.objects.create(
                    currency_id = item_transaction["currency"],
                    transaction = transaction,
                    quantity = item_transaction["quantity"]
                )
            serializer = TransactionDetailSerializer(transaction)
        except:
            return Response({"error": "Transaction Failed."} ,status=HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=HTTP_200_OK)

