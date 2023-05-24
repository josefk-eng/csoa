from django.shortcuts import render
from csoa import models


# Create your views here.
def overview(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, 'res_overview.html', {"moving": text, "movingword": word})

def familyLinks(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, 'family_links.html', {"moving": text, "movingword": word})


def bibleEngage(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, 'bible_engagements.html', {"moving": text, "movingword": word})


def covidRelief(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, 'covid19_relief.html', {"moving": text, "movingword": word})
