from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from account.forms import ProfileForm, UserForm
from account.models import Profile


@login_required(login_url="account:login")
def profile(request):
    user = request.user
    user_profile = get_object_or_404(Profile, user=user)
    if request.method == "POST":
        user_profile.directory = True if request.POST.get("directory") == 1 else False
        user_profile.dir_name = request.POST.get("dir_name")
        user_profile.dir_content = request.POST.get("dir_content").strip()
        user_profile.dir_phone = request.POST.get("dir_phone")
        user_profile.dir_email = request.POST.get("dir_email")
        user_profile.dir_website = request.POST.get("dir_website").strip()
        user_profile.dir_address1 = request.POST.get("dir_address1").strip()
        user_profile.dir_address2 = request.POST.get("dir_address2").strip()
        user_profile.dir_city_state_zip = request.POST.get("dir_city_state_zip").strip()
        user_profile.save()
        user.first_name = request.POST.get("first_name").strip()
        user.last_name = request.POST.get("last_name").strip()
        user.email = request.POST.get("email").strip()
        user.phone_number = request.POST.get("phone_number").strip()
        user.contact_by_phone = request.POST.get("contact_by_phone")
        user.save()
        messages.success(request, "Your profile has been updated")
        return redirect("account:dashboard")
    formp = ProfileForm(instance=user_profile)
    forma = UserForm(instance=user)
    p = Profile.objects.get(user=request.user)
    context = {
        "forma": forma,
        "formp": formp,
        "user_profile": user_profile,
        "directory": p.directory,
        "contact_by_phone": user.contact_by_phone,
    }
    return render(request, "account/profile.html", context)
