from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from account.models import Account


@login_required(login_url='account:login')
def change_pwd(request):
    if request.method == 'POST':
        current_pwd = request.POST['current_pwd']
        new_pwd = request.POST['new_pwd']
        confirm_new_pwd = request.POST['confirm_new_pwd']

        user = Account.objects.get(user=request.user)

        if new_pwd == confirm_new_pwd:
            success = user.check_password(current_pwd)
            if success:
                user.set_password(new_pwd)
                user.save()
                messages.success(request, 'Your password has been updated')
                return redirect('account:dashboard')
            else:
                messages.error(request, 'Your current password is incorrect')
                return redirect('account:change_pwd')
        else:
            messages.error(request, 'Your new / confirm password does not match')
    context = {}
    return render(request, 'account/change_pwd.html', context)
