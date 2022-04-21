from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Transaction, Transaction2, Trader, Product, Invoice, TgUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['url', 'title', 'user', 'content']


class TransactionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = ['id', 'time', 'json','user']

class Transaction2Serializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Transaction2
        fields = ['id', 'time', 'json','user']

class TraderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trader
        fields = ['uid','nick']

class ProductSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id','title','description','price', 'user']

class TgUserSerializer(serializers.ModelSerializer):
    # product = ProductSerializer(read_only=True)
    class Meta:
        model = TgUser
        fields = ['id', 'user_id', 'user_name', 'first_name', 'chat_id', 'product', 'condition', 'last_payment']

class InvoiceSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    class Meta:
        model = Invoice
        fields = ['id', 'product', 'status', 'address', 'uniq_id', 'chat_id', 'username', 'wallet', 'btcvalue', 'created_at', 'next_payment']