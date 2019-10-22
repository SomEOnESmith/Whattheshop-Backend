from django.contrib.auth.models import User
from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from .models import Crypto, Profile, Transaction, TransactionItem



class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        new_user = User(**validated_data)
        new_user.set_password(validated_data['password'])
        new_user.save()
        new_profile = Profile.objects.create(user=new_user)
        new_profile.save()
        return validated_data


class CurrencyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [  
            'username',
            'first_name',
            'last_name',
            'email',
        ]
#  newwwwwww
class TransactionSerializer(serializers.ModelSerializer):
        class Meta:
            model = Transaction
            fields = "__all__"

# newwwwwwww
class ItemTransactionSerializer(serializers.ModelSerializer):

        class Meta: 
            model = TransactionItem
            fields = ["id","transaction", "quantity"]


# newwwwwww
class TransactionDetailSerializer(serializers.ModelSerializer):
    transaction_items = ItemTransactionSerializer(many=True);


    class Meta:
        model = Transaction
        fields = "__all__"

# //////////////////////////////////////////////////////////////////////
class ProfileDetailViewSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    tranactions = TransactionDetailSerializer(many=True)
    class Meta:
        model = Profile
        fields = [  
            'user',
            'image',
            'phone_number',
            'birth_date',
            'tranactions'
        ]   
        


        def get_past_orders(self, obj):
            orders = Transaction.objects.filter(user=obj.user, date__lt=date.today())
            return OrderSerializer(orders, many=True).data





class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        # token['birth_date'] = user.profile.birth_date
        # token['phone_number'] = user.profile.phone_number
        # token['image'] = user.profile.image.url
        
        return token

# class CreditCardSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CreditCard
#         fields = "__all__"

#  ////////////////////////////////////////////////////////////////////////////////////
# after ordering (history)

# class WalletSerializer(serializers.ModelSerializer):
#     product = TransactionSerializer()
#     class Meta:
#         model = Transaction
#         fields = '__all__'