from django.urls import path

from core import views

app_name = "core"
urlpatterns = [
    path("", views.home, name="home"),
    path("policies/", views.policies, name="policies"),
    path("contact_us/", views.contact_us, name="contact_us"),
    path("faq/", views.faq, name="faq"),
    path("set_faq/", views.set_faq, name="set_faq"),
    path("set_policies/", views.set_policies, name="set_policies"),
    path("payment/", views.payment, name="payment"),
    path("success/<int:order_number>/", views.success, name="success"),
    path("cancel/<int:order_number>/", views.cancel, name="cancel"),
    path("checkout/", views.checkout, name="checkout"),
    path("donate/", views.donate, name="donate"),
    path("webhook/", views.webhook, name="webhook"),
    path("communications/", views.communications, name="communications"),
]
