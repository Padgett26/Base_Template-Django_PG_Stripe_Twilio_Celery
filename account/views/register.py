import random

from django.shortcuts import render

from account.forms import RegistrationForm
from account.models import Account, Profile
from account.tasks import send_mail, send_sms


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            phone_number = form.cleaned_data.get("phone_number")
            contact_by_phone = form.cleaned_data.get("contact_by_phone")
            verify_code = random.Random().choice(range(100000, 999999))
            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                phone_number=phone_number,
                contact_by_phone=contact_by_phone,
                verify_code=verify_code,
            )
            Profile.objects.create(user=user)

            message = "Please acivate you SFI account\r\n\r\n"
            message += "Enter this code to confirm:\r\n\r\n"
            message += verify_code
            message += "\r\n\r\nThank you,\r\n"
            message += "SFI Admin"
            mail_subject = "Please activate your SFI account"
            if user.contact_by_phone and user.phone_number > 1:
                send_sms.run(user.phone_number, message)
            else:
                user.contact_by_phone = False
                user.save()
                send_mail.run(mail_subject, message, user.email)
            context = {"user": user}
            return render(request, "account/verify_code.html", context)
    else:
        form = RegistrationForm()

    context = {
        "form": form,
    }
    return render(request, "account/register.html", context)
