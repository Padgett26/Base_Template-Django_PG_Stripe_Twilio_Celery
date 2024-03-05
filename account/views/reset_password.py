from django.contrib import messages
from django.shortcuts import redirect, render


def reset_password(request):
    if request.method == "POST":
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        if password == confirm_password:
            user = request.user
            user.set_password(password)
            user.save()
            messages.success(request, "Your password has been updated")
            return redirect("core:home")
        else:
            messages.error(request, "Passwords do not match")
            return redirect("account:reset_password")
    else:
        return render(request, "account/reset_password.html")
