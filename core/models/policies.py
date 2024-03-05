from django.db import models
from django.utils import timezone


class Policies(models.Model):
    title = models.CharField(max_length=100)
    policy = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Policies"
        verbose_name_plural = "Policies"
