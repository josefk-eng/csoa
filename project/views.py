from django.shortcuts import render
from csoa import models


# Create your views here.
def overview(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, 'projects_overview.html', {"moving": text, "movingword": word})


def examination(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, 'examination_board.html', {"moving": text, "movingword": word})


def seminars(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, 'academic_seminars.html', {"moving": text, "movingword": word})


def awarenessClimate(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, 'awarenes_climate_conservation.html', {"moving": text, "movingword": word})


def childrenInSchool(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, 'awarenes_children_stay_in_school.html', {"moving": text, "movingword": word})


def boyChild(request):
    return render(request, 'boy_child_awakening.html', {"moving": text, "movingword": word})


def discipleship(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, 'discipleship.html', {"moving": text, "movingword": word})


def girlChild(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, 'girl_child_empowerment.html', {"moving": text, "movingword": word})


def menstrual(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, 'menstrual_health.html')


def prayerNet(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, 'prayer_networks.html')


def regionalMDD(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, 'regional_MDD.html')


def regionalSportsGalour(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, 'regional_sports_galour.html')
