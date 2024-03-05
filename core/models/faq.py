from django.db import models
from django.utils import timezone


class FAQ(models.Model):
    question = models.CharField(max_length=200, unique=True)
    answer = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
