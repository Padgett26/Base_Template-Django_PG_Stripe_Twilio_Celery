from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='account:login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return render(request, 'account/login.html')
