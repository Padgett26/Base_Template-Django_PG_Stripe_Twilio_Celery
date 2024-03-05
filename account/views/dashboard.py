from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from account.models import Profile
from core.models import Transaction


@login_required(login_url="account:login")
def dashboard(request):
    user = request.user
    user_profile = Profile.objects.get(user=user)
    transactions = Transaction.objects.filter(payer=user).order_by("created_at")
    context = {
        "user_profile": user_profile,
        "transactions": transactions,
    }
    return render(request, "account/dashboard.html", context)
