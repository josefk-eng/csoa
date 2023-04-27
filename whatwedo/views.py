from django.shortcuts import render
from csoa import models


# Create your views here.
def prayer(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, 'prayer.html', {"moving": text, "movingword": word})


def stories(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, 'our_stories.html', {"moving": text, "movingword": word})


def partnership(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, 'partnership.html', {"moving": text, "movingword": word})


def testimonial(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, 'what_they_say.html', {"moving": text, "movingword": word})


def news(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, 'news.html', {"moving": text, "movingword": word})
