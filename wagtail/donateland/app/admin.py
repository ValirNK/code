from django.contrib import admin
from .models import Transaction, Transaction2, Trader, Product, Invoice, TgUser
# Register your models here.

class TransactionAdmin(admin.ModelAdmin):
    model = 'Transaction'
    list_display = ('id', 'time', 'json')
    search_fields = ['json']

class Transaction2Admin(admin.ModelAdmin):
    model = 'Transaction2'
    list_display = ('id', 'time', 'json')
    search_fields = ['json']


class TraderAdmin(admin.ModelAdmin):
    model = 'Trader'
    list_display = ('id', 'uid', 'nick')
    search_fields = ['uid']

class ProductAdmin(admin.ModelAdmin):
    model = 'Product'
    list_display = ('id', 'title', 'description','price')
    search_fields = ['title']

class InvoiceAdmin(admin.ModelAdmin):
    model = 'Invoice'
    list_display = ('id','product', 'status', 'address', 'uniq_id', 'chat_id', 'username', 'wallet', 'btcvalue', 'created_at', 'next_payment')
    search_fields = ['product']

class TgUserAdmin(admin.ModelAdmin):
    model = 'TgUser'
    list_display = ('user_name', 'chat_id', 'product', 'condition', 'last_payment')
    search_fields = ['user_name']

admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Transaction2, Transaction2Admin)
admin.site.register(Trader, TraderAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(TgUser, TgUserAdmin)
admin.site.register(Product, ProductAdmin)