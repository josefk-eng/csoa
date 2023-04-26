from django.shortcuts import render
from csoa.models import MovingText, MovingWord


# Create your views here.
def network(request):
    text = MovingText.objects.all()
    word = MovingWord.objects.all()
    context = {"moving": text, "movingword": word}
    return render(request, 'cordinatornetwork.html', context)


def statements(request):
    text = MovingText.objects.all()
    word = MovingWord.objects.all()
    context = {"moving": text, "movingword": word}
    return render(request, 'statements.html', context)


def history(request):
    text = MovingText.objects.all()
    word = MovingWord.objects.all()
    context = {"moving": text, "movingword": word}
    return render(request, 'history.html', context)


def partners(request):
    text = MovingText.objects.all()
    word = MovingWord.objects.all()
    context = {"moving": text, "movingword": word}
    return render(request, 'partners', context)


def modeofoperation(request):
    text = MovingText.objects.all()
    word = MovingWord.objects.all()
    context = {"moving": text, "movingword": word}
    return render(request, 'modeofoperations.html', context)


def portfolios(request):
    text = MovingText.objects.all()
    word = MovingWord.objects.all()
    context = {"moving": text, "movingword": word}
    return render(request, 'portfolios.html', context)