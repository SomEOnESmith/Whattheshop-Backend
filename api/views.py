from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import render
from rest_framework import status

from .serializers import UserCreateSerializer, CurrencyListSerializer,ProfileDetailViewSerializer, MyTokenObtainPairSerializer, ItemTransactionSerializer, TransactionDetailSerializer
from .models import Crypto, Profile, Transaction, TransactionItem

from datetime import datetime


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class CryptoListAPIView(ListAPIView):
    queryset = Crypto.objects.all()
    serializer_class = CurrencyListSerializer


class ProfileDetailAPIView(APIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailViewSerializer
    permission_classes = [IsAuthenticated]
    # /////////////////
    def get(self, request):
        profile = Profile.objects.get(user=self.request.user)
        serializer_class = ProfileDetailViewSerializer(profile, context={"request": request})
        return Response(serializer_class.data, status = status.HTTP_200_OK)


    def put(self, request):
        profile = Profile.objects.get(user=self.request.user)
        serializer_class = ProfileDetailViewSerializer(data=request.data, instance=profile)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status = status.HTTP_200_OK)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
# ////////////////////////


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CheckoutCart(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):

        profile = request.user.profile
        transaction = Transaction.objects.create(profile=profile)
        try:
            total=0.0
            for item_transaction in request.data:
                crypto = Crypto.objects.get(id=item_transaction["currency"])
                item_transaction["quantity"] = float(item_transaction["quantity"])
                transaction_item = TransactionItem.objects.create(
                    currency_id = item_transaction["currency"],
                    transaction = transaction,
                    quantity = item_transaction["quantity"]
                )
                total= total + (float(crypto.price)*float(transaction_item.quantity))
            transaction.datetime=datetime.now()
            transaction.total=total
            transaction.save()
            serializer = TransactionDetailSerializer(transaction)
        except:
            return Response({"error": "Transaction Failed."} ,status=HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=HTTP_200_OK)

