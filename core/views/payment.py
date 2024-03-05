import stripe
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from core.models import Transaction
from sfi.settings import STRIPE_SECRET_KEY, SITE_URL


@login_required(login_url="account/login/")
def payment(request):
    stripe.api_key = STRIPE_SECRET_KEY
    if request.method == "POST":
        order_number = request.POST.get("order_number")
        trans = Transaction.objects.filter(order_id=order_number).first()
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price": trans.price_id,
                    "quantity": 1,
                }
            ],
            mode="payment",
            metadata={"order_number": order_number},
            success_url="https://" + SITE_URL + "/success/" + order_number + "/",
            cancel_url="https://" + SITE_URL + "/cancel/" + order_number + "/",
        )
        return redirect(checkout_session.url, code=303)
