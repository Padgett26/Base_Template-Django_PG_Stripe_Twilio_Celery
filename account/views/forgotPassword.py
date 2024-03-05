import random

from django.contrib import messages
from django.shortcuts import render, redirect

from account.models import Account
from account.tasks import send_mail, send_sms


def forgotPassword(request):
    if request.method == "POST":
        contact = request.POST["contact"]
        if Account.objects.filter(email=contact).exists():
            user = Account.objects.get(email__iexact=contact)
        elif Account.objects.filter(phone_number=contact).exists():
            user = Account.objects.get(phone_number__iexact=contact)
        else:
            user = None

        if user is not None:
            verify_code = random.Random().choice(range(100000, 999999))
            message = "Password rest verification code\r\n\r\n"
            message += "Enter this code to confirm:\r\n\r\n"
            message += verify_code + "\r\n\r\n"
            message += "Thank you,\r\n"
            message += "SFI Admin"
            mail_subject = "Password rest verification code"
            if user.contact_by_phone and user.phone_number > 1:
                send_sms.run(user.phone_number, message)
            else:
                user.contact_by_phone = False
                user.save()
                send_mail.run(mail_subject, message, user.email)
            context = {"user": user}
            return render(request, "account/verify_forgot.html", context)
        else:
            messages.error(request, "I couldn't find you in our system.")
            return redirect("account:forgotPassword")
    return render(request, "account/forgotPassword.html")
