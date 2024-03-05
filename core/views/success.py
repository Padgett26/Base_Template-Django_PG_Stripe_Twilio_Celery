from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from core.models import Transaction


@login_required(login_url="account/login/")
def success(
    request,
):
    if request.method == "GET":
        order_number = request.GET.get("order_number")
        trans = Transaction.objects.get(order_id=order_number)
        trans.status = "checkout"
        trans.save()
        context = {
            "order_number": order_number,
        }
        return render(request, "core/success.html", context)
