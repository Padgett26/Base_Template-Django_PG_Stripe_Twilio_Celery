from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

from core.models import Policies


@staff_member_required(login_url="/account/login")
def set_policies(request):
    if request.method == "POST":
        p_id = request.POST.get("p_id")
        title = request.POST.get("title")
        policy = request.POST.get("policy")
        active = request.POST.get("active")
        delete = request.POST.get("delete")
        if p_id == "new":
            Policies.objects.create(title=title, policy=policy, active=active)
        else:
            if delete == "1":
                Policies.objects.get(id=p_id).delete()
            else:
                update = Policies.objects.get(pk=p_id)
                update.title = title
                update.policy = policy
                update.active = active
                update.save()
    p = Policies.objects.all()
    context = {
        "policies": p,
    }
    return render(request, "core/set_policies.html", context)
