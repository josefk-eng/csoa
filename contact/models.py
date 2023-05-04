from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    body = models.CharField(max_length=2000)

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contact")

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("Contact_detail", kwargs={"pk": self.pk})
