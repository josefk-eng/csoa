from django.shortcuts import render
from csoa import models

# Create your views here.
def leadership(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, 'leadership.html', {"moving": text, "movingword": word})


def schoolMgt(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, 'school_mgt_trainings.html', {"moving": text, "movingword": word})


def itAndAuto(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, 'it_automation.html', {"moving": text, "movingword": word})


def financialLiteracy(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, 'financial_literacy.html', {"moving": text, "movingword": word})


def capacityBuilding(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, 'capacity_building.html', {"moving": text, "movingword": word})
