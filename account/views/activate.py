from django.contrib import auth
from django.contrib import messages
from django.shortcuts import redirect

from account.models import Account


def activate(request):
    verify_code = request.POST.get("verify_code")
    email = request.POST.get("email")
    user = Account.objects.get(email=email)
    if user.verify_code == verify_code:
        user.verify_code = 0
        user.is_active = True
        user.save()
        auth.login(request, user)
        messages.success(request, "You are now logged in")
        return redirect("account:dashboard")
    else:
        user.delete()
        messages.error(
            request,
            "Invalid verification code, please re-register to receive a new code",
        )
        return redirect("account:register")
