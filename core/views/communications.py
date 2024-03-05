from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.template.loader import render_to_string

from account.models import Account
from account.tasks import send_mail
from core.models import Contact


@staff_member_required(login_url="/account/login")
def communications(request):
    if request.method == "POST":
        comm_id = request.POST["comm_id"]
        reply = request.POST["reply"]
        comm = Contact.objects.get(id=comm_id)
        comm.reply = reply
        comm.reply_by = request.user.username
        comm.archived = True
        comm.save()
        user = Account.objects.get(pk=comm.sent_by.pk)
        mail_subject = "A reply to your communication with cncobulletinboard.com"
        message = render_to_string(
            "core/contact_us_reply.html",
            {"user": user, "reply": reply, "reply_by": request.user.full_name()},
        )
        send_mail.delay(mail_subject, message, user.email)
        messages.success(request, "Reply email sent")
    c = Contact.objects.filter(archived=False).order_by("created_date")
    context = {"contacts": c}
    return render(request, "core/communications.html", context)
