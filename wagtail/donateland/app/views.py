from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .serializers import UserSerializer, PostSerializer, TransactionSerializer, Transaction2Serializer, TraderSerializer, ProductSerializer, InvoiceSerializer, TgUserSerializer
from . import models
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from .models import Transaction, Product
import json
import redis
import time
# import fsm.app.handlers.common
import os
global data

r = redis.StrictRedis(
    host='127.0.0.1',
    port=6379,
    charset="utf-8",
    decode_responses=True
) 

@csrf_exempt
def init(request, **kwargs):
    print('-------------------------')
    data = json.loads(list(request.POST.items())[0][0])
    unixtime = int(time.time())
    t = Transaction(time=str(unixtime), json=data)
    t.save()
    r.set('last_updated', str(data))
    print('--------------------------')
    return HttpResponse(request)

@csrf_exempt
def locale(request, **kwargs):
    language = request.GET['locale']
    with open(os.getcwd()+'\\app\\fsm\\locales.json', 'r', encoding='utf-8') as loc:
        locale = json.load(loc)
    return HttpResponse(json.dumps(locale[language]), content_type="application/json")

@api_view(['POST'])
def CreateInvoice(request):
    data = request.data
    user = request.user
    invoice = models.Invoice.create(
        product = data["product"],
        status = 0,
        address = "",
        uniq_id= "",
        chat_id= "",
        username= "",
        wallet = "btc",
        btcvalue= 2.3e-05,
        created_at= "1637446155"
    )
    print("request", request)
    serializer = InvoiceSerializer(invoice, many=False)
    return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['POST', 'GET'])
    def comments(self, request, pk):
        post = models.Post.objects.get(pk=pk)
        if request.method == 'GET':
            self.serializer_class = CommentSerializer
            queryset = models.Comment.objects.filter(post=post);
            serializer = CommentSerializer(queryset, many=True, context={'request': request})
            return Response(serializer.data)
        else:
            self.serializer_class = CommentSerializer
            queryset = models.Comment.objects.filter(post=post);
            serializer = CommentSerializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user, post=post)
            return Response(serializer.data)

    @action(detail=False, methods=['DELETE'])
    def remove_comment(self, request, pk, comment):
        comment = models.Comment.objects.get(pk=comment)
        if comment.delete():
            return Response({'message':'Comment deleted'})
        else:
            return Response({'message':'unable to delete comment'})

    def create(self, request):
        serializer = PostSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True) # check all fields is valid before attempting to save
        serializer.save(user=request.user)
        return Response(serializer.data)

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = models.Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['GET'])
    def transaction(self, request, pk):
        transaction = models.Transaction.objects.get(id=pk)
        self.serializer_class = TransactionSerializer
        queryset = models.Transaction.objects.filter(id=pk);
        serializer = TransactionSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

class Transaction2ViewSet(viewsets.ModelViewSet):
    queryset = models.Transaction2.objects.all()
    serializer_class = Transaction2Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['POST', 'GET'])
    def transaction(self, request, pk):
        transaction = models.Transaction2.objects.get(id=pk)
        self.serializer_class = Transaction2Serializer
        queryset = models.Transaction2.objects.filter(id=pk);
        serializer = TransactionSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

class TraderViewSet(viewsets.ModelViewSet):
    queryset = models.Trader.objects.all()
    serializer_class = TraderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'uid'
    @action(detail=False, methods=['GET'])
    def trader(self, request, uid):
        print('-----------')
        print(uid)
        trader = models.Trader.objects.get(uid=uid)
        self.serializer_class = TraderSerializer
        queryset = models.Trader.objects.filter(uid=uid);
        serializer = TraderSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'id'
    @action(detail=False, methods=['GET'])
    def trader(self, request, id):
        product = models.Product.objects.get(id=id)
        self.serializer_class = ProductSerializer
        queryset = models.Product.objects.filter(id=id);
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = models.Invoice.objects.all()
    serializer_class = InvoiceSerializer
    http_method_names = ['get', 'post', 'head', 'put']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'address'
    @action(detail=False, methods=['GET'])
    def inv(self, request, address):
        invoice = models.Invoice.objects.get(address=address)
        self.serializer_class = InvoiceSerializer
        serializer = InvoiceSerializer(invoice, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        serializer = InvoiceSerializer(
            data=request.body, context={'request': request})
        serializer.is_valid(raise_exception=True) # check all fields is valid before attempting to save
        serializer.save()
        return Response(serializer.data)

class TgUserViewSet(viewsets.ModelViewSet):
    queryset = models.TgUser.objects.all()
    serializer_class = TgUserSerializer
    http_method_names = ['get', 'post', 'head', 'put']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'chat_id'
    @action(detail=False, methods=['GET'])
    def tguser(self, request, chat_id):
        tguser = models.TgUser.objects.filter(chat_id=chat_id)
        serializer = self.serializer_class(tguser, many=True, context={'request': request})
        return Response(serializer.data)

class MakeInvoice(APIView):
    def post(self, request):
        serializer = InvoiceSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True) # check all fields is valid before attempting to save
        serializer.save()
        return Response(serializer.data)

class DeleteInvoice(viewsets.ModelViewSet):
    queryset = models.Invoice.objects.all()
    serializer_class = InvoiceSerializer
    http_method_names = ['get', 'post', 'head', 'put', 'delete']
    lookup_field = 'address'
    @action(detail=False, methods=['GET'])
    def inv(self, request, address):
        invoice = models.Invoice.objects.filter(address=address)
        self.serializer_class = InvoiceSerializer
        serializer = InvoiceSerializer(invoice, many=True, context={'request': request})
        return Response(serializer.data)
    def destroy(self, request, address, *args, **kwargs):
        instance = models.Invoice.objects.get(address=address)
        print(address)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MakeTgUser(APIView):
    def post(self, request):
        serializer = TgUserSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True) # check all fields is valid before attempting to save
        serializer.save()
        return Response(serializer.data)

class GetTgUser(generics.ListAPIView):
    lookup_field = 'chat_id'
    serializer_class = TgUserSerializer
    def list(self, request, chat_id):
        tguser = models.TgUser.objects.get(chat_id=chat_id)
        serializer = self.serializer_class(tguser, many=True, context={'request': request})
        return Response(serializer.data)

class UpdateTgUser(generics.UpdateAPIView):
    lookup_field = 'chat_id'
    serializer_class = TgUserSerializer
    def update(self, request, **kwargs):
        tgusers = models.TgUser.objects.all()
        tguser = get_object_or_404(tgusers, chat_id=request.data["chat_id"])
        serializer = self.serializer_class(tguser, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)

class UpdateInvoice(generics.UpdateAPIView):
    lookup_field = 'address'
    serializer_class = InvoiceSerializer
    authentication_classes = []
    @method_decorator(ensure_csrf_cookie)
    def get(self, request, address):
        invoice = models.Invoice.objects.get(address=address)
        self.serializer_class = InvoiceSerializer
        serializer = InvoiceSerializer(invoice, many=True, context={'request': request})
        return Response(serializer.data)
    @method_decorator(ensure_csrf_cookie)
    def update(self, request, **kwargs):
        invoices = models.Invoice.objects.all()
        inv = get_object_or_404(invoices, address=request.data["address"])
        serializer = self.serializer_class(inv, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)
