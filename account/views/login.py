from django.contrib import auth
from django.contrib import messages
from django.shortcuts import redirect, render


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect("account:dashboard")
        else:
            messages.error(request, "Invalid log in credentials")
            return redirect("account:login")
    context = {}
    return render(request, "account/login.html", context)
