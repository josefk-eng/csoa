from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


# Create your models here.
class News(models.Model):
    image = models.ImageField(upload_to="img/news", default="img/placeholder.jpeg")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("News_detail", kwargs={"pk": self.pk})


class Prayer(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Prayer")
        verbose_name_plural = _("Prayer")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Prayer_detail", kwargs={"pk": self.pk})


class Testimonial(models.Model):
    image = models.ImageField(upload_to="img/tests", default="img/placeholder.jpeg")
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    testimony = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Testimonial")
        verbose_name_plural = _("Testimonial")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Testimonial_detail", kwargs={"pk": self.pk})


class Story(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="img/tests", default="img/placeholder.jpeg")
    url = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    isMain = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Story")
        verbose_name_plural = _("Story")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Story_detail", kwargs={"pk": self.pk})

