from django.contrib import messages
from django.shortcuts import render

from core.forms import ContactForm
from core.models import Contact


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            cu = Contact.objects.create(
                sent_by=request.user,
                subject=subject,
                message=message,
            )
            cu.save()
            messages.success(request, 'You message has been saved. Thank you for contacting us.')
            return render(request, 'core/contact_us.html', {'subject': subject, 'message': message, 'done': True})
    form = ContactForm()
    context = {'form': form}
    return render(request, 'core/contact_us.html', context)
