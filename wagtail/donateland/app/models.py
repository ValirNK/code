from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Transaction(models.Model):
    time = models.CharField(max_length=200)
    json = models.JSONField(null=True, blank=True)

class Transaction2(models.Model):
    time = models.CharField(max_length=200)
    json = models.JSONField(null=True, blank=True)

class Trader(models.Model):
    uid = models.CharField(max_length=50)
    nick = models.CharField(max_length=50)

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.title

class Invoice(models.Model):
    STATUS_CHOICES = ((0,"Не оплачен"), (1,"Оплачен"))
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    address = models.CharField(max_length=250, blank=True, null=True)
    btcvalue = models.FloatField(blank=True, null=True)
    # received = models.FloatField(blank=True, null=True)
    # txid = models.CharField(max_length=250, blank=True, null=True)
    # rbf = models.IntegerField(blank=True, null=True)
    created_at = models.CharField(max_length=250, blank=True)
    next_payment = models.CharField(max_length=250, blank=True)
    uniq_id = models.CharField(max_length=250, blank=True)
    chat_id = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=250, blank=True)
    wallet = models.CharField(max_length=40, blank=True)

    def __str__(self):
        if not self.address is None:
            return self.address
        else:
            return self.chat_id

class TgUser(models.Model):
    user_id = models.CharField(max_length=50, blank=True)
    user_name = models.CharField(max_length=150, blank=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    chat_id = models.CharField(max_length=50, blank=True)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    condition = models.CharField(max_length=5, default='off')
    last_payment = models.DateField()
    date_click = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user_id