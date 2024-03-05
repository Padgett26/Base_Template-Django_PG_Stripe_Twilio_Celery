from django.shortcuts import render

from core.models import FAQ


def faq(request):
    f = FAQ.objects.filter(active=True)
    context = {
        "faqs": f,
    }
    return render(request, "core/faq.html", context)
