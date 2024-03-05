from django.shortcuts import render

from core.models import Policies


def policies(request):
    p = Policies.objects.filter(active=True)
    context = {
        "policies": p,
    }
    return render(request, "core/policies.html", context)
