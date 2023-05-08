from django.shortcuts import render
from csoa.models import MovingText, MovingWord, Partners, Header
from . import models


# Create your views here.
def network(request):
    text = MovingText.objects.all()
    word = MovingWord.objects.all()
    head = Header.objects.all()
    port = models.Portfolio.objects.all()
    context = {"moving": text, "movingword": word, "heads": head, "portfolio":port}
    return render(request, 'cordinatornetwork.html', context)


def statements(request):
    text = MovingText.objects.all()
    word = MovingWord.objects.all()
    stats = models.Statement.objects.all()
    head = Header.objects.all()
    context = {"moving": text, "movingword": word, "states": stats, "heads": head}
    return render(request, 'statements.html', context)


def history(request):
    text = MovingText.objects.all()
    word = MovingWord.objects.all()
    hist = models.History.objects.all()
    head = Header.objects.all()
    context = {"moving": text, "movingword": word, "history": hist, "heads": head}
    return render(request, 'history.html', context)


def partners(request):
    text = MovingText.objects.all()
    word = MovingWord.objects.all()
    part = Partners.objects.all()
    head = Header.objects.all()
    context = {"moving": text, "movingword": word, "partners": part, "heads": head}
    return render(request, 'partners.html', context)


def modeofoperation(request):
    text = MovingText.objects.all()
    word = MovingWord.objects.all()
    head = Header.objects.all()
    context = {"moving": text, "movingword": word, "heads": head}
    return render(request, 'modeofoperations.html', context)


def portfolios(request):
    text = MovingText.objects.all()
    word = MovingWord.objects.all()
    port = models.Portfolio.objects.all()
    head = Header.objects.all()
    context = {"moving": text, "movingword": word, "portfolios": port, "heads": head}
    return render(request, 'portfolios.html', context)
