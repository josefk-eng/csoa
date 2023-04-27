from django.shortcuts import render
from csoa import models


# Create your views here.
def contact(request):
    text = models.MovingText.objects.all()
    word = models.MovingWord.objects.all()
    return render(request, "contact.html", {"moving": text, "movingword": word})
