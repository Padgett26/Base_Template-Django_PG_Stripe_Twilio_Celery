import datetime

import stripe
from django.shortcuts import render

from core.models import Transaction, Company
from sfi.settings import STRIPE_SECRET_KEY


def checkout(request):
    if request.method == "POST":
        u = request.user
        c = Company.objects.all().first()
        amount = int(request.POST.get("amount"))
        amt = amount * 100
        stripe.api_key = STRIPE_SECRET_KEY
        if c.stripe_prod_id:
            prod_id = c.stripe_prod_id
        else:
            prod = stripe.Product.create(
                name="Donate",
                metadata={"internal_id": u.id},
            )
            prod_id = prod["id"]
            c.stripe_prod_id = prod_id
            c.save()

        price = stripe.Price.create(
            unit_amount=amt,
            currency="usd",
            product=prod_id,
        )
        trans = Transaction()
        trans.payer = request.user
        trans.amount = amount
        trans.price_id = price["id"]
        trans.save()

        yr = int(datetime.date.today().strftime("%Y"))
        dt = int(datetime.date.today().strftime("%d"))
        mt = int(datetime.date.today().strftime("%m"))
        d = datetime.date(yr, mt, dt)
        current_date = d.strftime("%Y%m%d")
        order_number = current_date + str(trans.id)
        trans.order_id = order_number
        trans.save()

        context = {"order_number": order_number, "amount": amount}
        return render(request, "core/checkout.html", context)
