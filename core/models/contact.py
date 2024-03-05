from django.db import models

from account.models import Account


class Contact(models.Model):
    sent_by = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    reply = models.TextField(default='', blank=True)
    reply_by = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    reply_date = models.DateTimeField(auto_now=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = "Contacts"
