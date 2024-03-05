from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default="To do")
    logo = models.ImageField(upload_to="page_pics", blank=True)
    email = models.EmailField()
    stripe_prod_id = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Company"
