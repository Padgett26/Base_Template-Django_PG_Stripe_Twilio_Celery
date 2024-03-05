from django.contrib import auth
from django.contrib import messages
from django.shortcuts import redirect

from account.models import Account


def resetpwd_validate(request):
    verify_code = request.POST.get("verify_code")
    email = request.POST.get("email")
    user = Account.objects.get(email=email)
    if user.verify_code == verify_code:
        user.verify_code = 0
        user.is_active = True
        user.save()
        auth.login(request, user)
        messages.success(request, "Please enter a new password")
        return redirect("account:reset_password")
    else:
        user.delete()
        messages.error(
            request,
            "Invalid verification code, please try again to receive a new code",
        )
        return redirect("account:forgotPassword")
