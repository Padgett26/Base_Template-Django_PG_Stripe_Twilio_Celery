from django.shortcuts import render

from core.models import Transaction


def cancel(request, order_number):
    Transaction.objects.get(order_id=order_number).delete()
    return render(request, "core/cancel.html")
