from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Wallet, WalletTransaction

@login_required(login_url='/accounts/login/')
def wallet_dashboard(request):
    # Safely get or create the user's wallet
    wallet, created = Wallet.objects.get_or_create(user=request.user)
    
    # Fetch wallet transactions
    transactions = WalletTransaction.objects.filter(wallet=wallet).order_by('-timestamp')
    
    return render(request, 'wallet/dashboard.html', {
        'wallet': wallet,
        'transactions': transactions,
    })
