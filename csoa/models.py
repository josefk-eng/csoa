from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


# Create your models here.
class MovingText(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("MovingText")
        verbose_name_plural = _("MovingText")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("MovingText_detail", kwargs={"pk": self.pk})


class MovingWord(models.Model):
    movingText = models.ForeignKey(MovingText, on_delete=models.CASCADE)
    word = models.CharField(max_length=500)
    isLink = models.BooleanField()
    linkAddress = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name = _("MovingWord")
        verbose_name_plural = _("MovingWord")

    def __str__(self):
        return self.word

    def get_absolute_url(self):
        return reverse("MovingWord_detail", kwargs={"pk": self.pk})


class Slider(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="img/slider")
    btn = models.CharField(max_length=100)
    btn_link = models.CharField(max_length=500)
    color = models.CharField(max_length=20,choices=[("blue", "blue"), ("brown", "brown"), ("orange", "orange"), ("purple", "purple")])

    class Meta:
        verbose_name = _("Slider")
        verbose_name_plural = _("Slider")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Slider_detail", kwargs={"pk": self.pk})
