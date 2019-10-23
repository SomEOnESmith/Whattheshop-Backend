from django.contrib.auth.models import User
from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from .models import Crypto, Profile, Transaction, TransactionItem



class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']

    def create(self, validated_data):
        new_user = User(**validated_data)
        print(new_user)
        new_user.set_password(validated_data['password'])
        new_user.save()
        profile = Profile.objects.get(user=new_user)
        profile.phone_number = self.context['request'].data['phone_number']
        profile.save()
        return validated_data


class CurrencyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]


class ItemTransactionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = TransactionItem
        fields = ["id","transaction", "quantity", "currency"]



class TransactionDetailSerializer(serializers.ModelSerializer):
    transaction_items = ItemTransactionSerializer(many=True);


    class Meta:
        model = Transaction
        fields = "__all__"


class ProfileDetailViewSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    transactions = TransactionDetailSerializer(many=True)
    
    class Meta:
        model = Profile
        fields = [  
            'user',
            'image',
            'phone_number',
            'birth_date',
            'transactions'
        ] 
        read_only_fields = ['username','transactions']
  # ////////////
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        transactions_data = validated_data.pop('transactions')
        instance.user.last_name = user_data.get('last_name', user_data['last_name'])
        instance.user.email = user_data.get('email', user_data['email'])
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.image = validated_data.get('image', instance.image)
        instance.user.save()
        instance.save()
        return instance
  # ///////////




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email        
        return token
