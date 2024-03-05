from django.db import models

from account.models import Account


class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100, default="My Business")
    content = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email_address = models.EmailField(max_length=100, null=True, blank=True)
    website = models.URLField(max_length=100, null=True, blank=True)
    address1 = models.CharField(max_length=100, null=True, blank=True)
    address2 = models.CharField(max_length=100, null=True, blank=True)
    city_state_zip = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"
