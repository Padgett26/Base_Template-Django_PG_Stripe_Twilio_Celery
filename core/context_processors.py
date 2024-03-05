from core.models import Company, Contact


def company_info(request):
    c = Company.objects.all().order_by("id").first()
    return {
        "company": c,
    }


def comm_count(request):
    cc = Contact.objects.filter(archived=False).count()
    return {
        "comm_count": cc,
    }
