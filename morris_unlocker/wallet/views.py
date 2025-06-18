from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def wallet_dashboard(request):
    return render(request, 'wallet/wallet_dashboard.html')

def statement(request):
    return render(request, 'wallet/statement.html')

def invoices(request):
    return render(request, 'wallet/invoices.html')

def voucher(request):
    return render(request, 'wallet/recharge_voucher.html')