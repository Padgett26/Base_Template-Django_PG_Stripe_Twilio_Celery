from django.contrib import admin

from core.models import Company, Contact, FAQ, Policies, Transaction

# Register your models here.
admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(FAQ)
admin.site.register(Policies)
admin.site.register(Transaction)
