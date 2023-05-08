from django.shortcuts import render
from csoa import models
from .models import News, Prayer, Testimonial, Story


# Create your views here.
def prayer(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    prayer = Prayer.objects.all()
    return render(request, 'prayer.html', {"moving": text, "movingword": word, "prayers":prayer})


def stories(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    story = Story.objects.all()
    return render(request, 'our_stories.html', {"moving": text, "movingword": word, "stories":story})


def partnership(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, 'partnership.html', {"moving": text, "movingword": word})


def testimonial(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    testimony = Testimonial.objects.all()
    return render(request, 'what_they_say.html', {"moving": text, "movingword": word, "testimonials":testimony})


def news(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    our_news = News.objects.all()
    head = models.Header.objects.all()
    return render(request, 'news.html', {"moving": text, "movingword": word, "news":our_news, "heads":head})
