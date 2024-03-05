from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage
from twilio.rest import Client

from jsg.settings import DONOT_REPLY_EMAIL


@shared_task()
def send_mail(subject, message, email):
    s = EmailMessage(
        subject,
        message,
        DONOT_REPLY_EMAIL,
        to=[
            email,
        ],
    )
    s.send()


@shared_task()
def send_sms(number, message):
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    client.messages.create(
        body="Join Earth's mightiest heroes. Like Kevin Bacon.",  # need to set
        from_="+17853329212",  # already set
        to="+15558675310",  # need to set
    )
