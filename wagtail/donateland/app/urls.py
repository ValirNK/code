from django.urls import path, include
from django.conf.urls import include, re_path, url
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'transactions', views.TransactionViewSet)
router.register(r'transactions2', views.Transaction2ViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'invoices', views.InvoiceViewSet)
router.register(r'tgusers', views.TgUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url(r'transaction/create$', view=views.init),
    # url(r'invoices/create/', view=views.CreateInvoice, name='invoice-create'),
    url(r'transactions/(?P<pk>\d+)/$', view=views.TransactionViewSet.as_view({'get': 'transaction'})),
    url(r'transactions2/(?P<pk>\d+)/$', view=views.Transaction2ViewSet.as_view({'get': 'transaction'})),
    url(r'locale/$', view=views.locale),
    url(r'traders/(?P<uid>(\d|\w)+)/$', view=views.TraderViewSet.as_view({'get': 'trader'})),
    url(r'posts/(?P<pk>\d+)/comments/$', view=views.PostViewSet.as_view({'get': 'comments', 'post': 'comments'})),
    url(r'posts/(?P<pk>\d+)/comments/(?P<comment>\d+)/$', view=views.PostViewSet.as_view({'delete': 'remove_comment'})),
    url(r'products/(?P<id>(\d)+)/$', view=views.ProductViewSet.as_view({'get': 'product'})),
    url(r'invoices/(?P<id>(\d|\w)+)/$', view=views.InvoiceViewSet.as_view({'get': 'inv'})),
    # url(r'invoices/create/', view=views.InvoiceViewSet.as_view({'put': 'create'}))
    url(r'create/invoice/', view=views.MakeInvoice.as_view(), name="invoice_create"),
    url(r'invoices/delete/(?P<address>(\d|\w|-)+)/$', view=views.DeleteInvoice.as_view({'delete':'destroy','get':'inv'})),
    url(r'tgusers/(?P<id>(\d)+)/$', views.GetTgUser.as_view(), name="tguser"),
    url(r'tgusers/update/(?P<id>(\d)+)/$', csrf_exempt(views.UpdateTgUser.as_view()), name="tguser_update"),
    url(r'invoices/update/(?P<address>(\d|\w|-)+)/$', views.UpdateInvoice.as_view(), name="invoice_update"),
    url(r'create/tguser/', view=views.MakeTgUser.as_view(), name="adduser")
]