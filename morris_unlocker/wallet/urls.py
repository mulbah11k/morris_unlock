from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/', views.wallet_dashboard, name='wallet_dashboard'),
    path('statement/', views.statement, name='my_statement'),
    path('invoices/', views.invoices, name='invoices'),
    path('voucher/', views.voucher, name='r_voucher'),
]
