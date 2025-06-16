from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def wallet_dashboard(request):
    return render(request, 'wallet/wallet_dashboard.html')