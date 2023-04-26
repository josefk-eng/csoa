from django.shortcuts import render
from . import models


# Create your views here.

def index(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    slider = models.Slider.objects.all()
    return render(request, 'home.html', {"moving": text, "movingword": word,"slider":slider})


def report(request):
    return render(request, 'report.html')
