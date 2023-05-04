from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)

    class Meta:
        verbose_name = _("Member")
        verbose_name_plural = _("Member")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Member_detail", kwargs={"pk": self.pk})


class Project(models.Model):
    name = models.CharField(max_length=100)
    cordinator = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=1000)
    big_description = models.CharField(max_length=2000)
    image = models.ImageField(upload_to="img/project", default="img/placeholder1.png")

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Project")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Project_detail", kwargs={"pk": self.pk})
