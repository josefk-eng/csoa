from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from project.models import Project, Member


# Create your models here.

class Statement(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    class Meta:
        verbose_name = _("Statement")
        verbose_name_plural = _("Statement")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Statement_detail", kwargs={"pk": self.pk})


class Values(models.Model):
    value = models.CharField(max_length=500)

    class Meta:
        verbose_name = _("Values")
        verbose_name_plural = _("Values")

    def __str__(self):
        return self.value

    def get_absolute_url(self):
        return reverse("Values_detail", kwargs={"pk": self.pk})


class History(models.Model):
    year = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="img/history", default="img/placeholder.jpeg")

    class Meta:
        verbose_name = _("History")
        verbose_name_plural = _("History")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("History_detail", kwargs={"pk": self.pk})


class Portfolio(models.Model):
    image = models.ImageField(upload_to="img/portfolio", default="img/placeholder.jpeg")
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Portfolio")
        verbose_name_plural = _("Portfolio")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Portfolio_detail", kwargs={"pk": self.pk})
