from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from project.models import Project, Member


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
    color = models.CharField(max_length=20,
                             choices=[("blue", "blue"), ("brown", "brown"), ("orange", "orange"), ("purple", "purple")])

    class Meta:
        verbose_name = _("Slider")
        verbose_name_plural = _("Slider")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Slider_detail", kwargs={"pk": self.pk})


class Introduction(models.Model):
    author = models.CharField(max_length=100)
    intro = models.CharField(max_length=500)
    visible = models.BooleanField(default=False)
    date_modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Introduction")
        verbose_name_plural = _("Introduction")

    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return reverse("Introduction_detail", kwargs={"pk": self.pk})


class Header(models.Model):
    head = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    section = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Header")
        verbose_name_plural = _("Header")

    def __str__(self):
        return self.section

    def get_absolute_url(self):
        return reverse("Header_detail", kwargs={"pk": self.pk})


class LatestEngagement(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="img/engagements", default="img/placeholder1.png")

    class Meta:
        verbose_name = _("LatestEngagement")
        verbose_name_plural = _("LatestEngagement")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("CSOAImages_detail", kwargs={"pk": self.pk})


class CSOAImages(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="img/images", default="img/placeholder1.png")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    engagement = models.ForeignKey(LatestEngagement, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = _("CSOAImages")
        verbose_name_plural = _("CSOAImages")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("CSOAImages_detail", kwargs={"pk": self.pk})


class CSOACards(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=2000)
    footer = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ForeignKey(CSOAImages, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = _("CSOACards")
        verbose_name_plural = _("CSOACards")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("CSOACards_detail", kwargs={"pk": self.pk})


class Partners(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="img/partners")
    description = models.CharField(max_length=1000)
    priority = models.IntegerField(default=0)

    class Meta:
        verbose_name = _("Partners")
        verbose_name_plural = _("Partners")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Partners_detail", kwargs={"pk": self.pk})


class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    director = models.ForeignKey(Member, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="img/schools", default="img/placeholder.jpeg")
    description = models.TextField(default="")

    class Meta:
        verbose_name = _("School")
        verbose_name_plural = _("School")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("School_detail", kwargs={"pk": self.pk})


class Subscriber(models.Model):
    firstName = models.CharField(max_length=100)
    secondName = models.CharField(max_length=100)
    email = models.EmailField(max_length=1000)
    region = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Subscriber")
        verbose_name_plural = _("Subscriber")

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("Subscriber_detail", kwargs={"pk": self.pk})


class Impact(models.Model):
    total = models.IntegerField()
    impacted = models.IntegerField()
    percent = models.IntegerField()
    card = models.ForeignKey(CSOACards, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Impact")
        verbose_name_plural = _("Impact")

    def __str__(self):
        return self.card.title

    def get_absolute_url(self):
        return reverse("Impact_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        self.percent = (self.impacted / self.total) * 100
        super().save(*args, **kwargs)


class Video(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    engagement = models.ForeignKey(LatestEngagement, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Video")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Video_detail", kwargs={"pk": self.pk})



