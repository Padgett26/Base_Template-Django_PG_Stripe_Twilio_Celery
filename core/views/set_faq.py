from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

from core.models import FAQ


@staff_member_required(login_url="/account/login")
def set_faq(request):
    if request.method == "POST":
        faq_id = request.POST.get("faq_id")
        question = request.POST.get("question")
        answer = request.POST.get("answer")
        active = request.POST.get("active")
        delete = request.POST.get("delete")
        if faq_id == "new":
            FAQ.objects.create(
                question=question,
                answer=answer,
                active=active,
            )
        else:
            if delete == "1":
                FAQ.objects.get(id=faq_id).delete()
            else:
                update = FAQ.objects.get(pk=faq_id)
                update.question = question
                update.answer = answer
                update.active = active
                update.save()
    f = FAQ.objects.all()
    context = {
        "faqs": f,
    }
    return render(request, "core/set_faq.html", context)
