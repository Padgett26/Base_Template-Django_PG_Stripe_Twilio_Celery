from django.shortcuts import render

from account.models import Profile


def search(request):
    if request.method == "POST":
        word = request.POST.get("word")
        dir_names = Profile.objects.filter(display_name__icontains=word, directory=True)
        dir_content = Profile.objects.filter(content__icontains=word, directory=True)
        context = {
            "word": word,
            "dir_names": dir_names,
            "dir_content": dir_content,
        }
        return render(request, "search/search.html", context)
    return render(request, "search/search.html")
