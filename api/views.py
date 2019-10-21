from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserCreateSerializer, CurrencyListSerializer,ProfileDetailViewSerializer, MyTokenObtainPairSerializer, TransactionSerializer, ItemTransactionSerializer, OrderSerializer
from .models import Crypto, Profile, Transaction, TransactionItem


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class CryptoListAPIView(ListAPIView):
    queryset = Crypto.objects.all()
    serializer_class = CurrencyListSerializer


# API view, that will grab the logged in users profile
class ProfileDetailAPIView(RetrieveAPIView):
    serializer_class = ProfileDetailViewSerializer

    def get(self, request, format=None):
        if request.user.is_anonymous:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        profile = ProfileSerializer(Profile.objects.get(user=request.user))
        return Response(profile.data, status=HTTP_200_OK)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# newwwwwwwwwwwww
class CheckoutCart(APIView):
        def post(self, request):
            transaction = Transaction.objects.create(user=request.user)
            try:
                for item_transaction in request.data:
                    ItemTransaction.objects.create(
                        item_id = item_transaction["item"],
                        transaction = transaction,
                        quantity = item_transaction["quantity"]
                    )
                serializer_class = OrderSerializer(transaction)
            except:
                return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer_class.data,status=status.HTTP_200_OK)
    




# class CreditCardView(APIView):
#     queryset = CreditCard.objects.all()
#     serializer_class = CreditCardSerializer
# create api view that prints whatever is recieving
# class PrintView(ListAPIView):
