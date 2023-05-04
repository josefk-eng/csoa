from django.shortcuts import render
from . import models


# Create your views here.

def index(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    slider = models.Slider.objects.all()
    intro = models.Introduction.objects.first()
    p = models.Project.objects.all()
    partner = models.Partners.objects.all()
    impact = models.Impact.objects.all()
    engags = models.LatestEngagement.objects.all()
    heads = models.Header.objects.all()
    return render(request, 'home.html', {"moving": text, "movingword": word, "slider": slider, "intro": intro,
                                         "projects": p[:6], "partners": partner[:8], "impacts": impact[:3], "engags":engags, "heads":heads})


def report(request):
    return render(request, 'report.html')
