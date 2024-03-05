import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from core.models import Transaction


@csrf_exempt
def webhook(request):
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    order_number = event["metadata"]["order_number"]
    trans = Transaction.objects.get(order_id=order_number)
    if event["type"] == "charge.pending":
        trans.status = "pending"
    if event["type"] == "charge.refunded":
        trans.status = "refunded"
    if event["type"] == "charge.expired":
        trans.status = "expired"
    if event["type"] == "charge.captured":
        trans.status = "captured"
    if event["type"] == "charge.failed":
        trans.status = "failed"
    if event["type"] == "charge.succeeded":
        trans.status = "succeeded"
    trans.save()

    return HttpResponse(status=200)
