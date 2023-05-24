from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.overview, name='res_overview'),
    path('family_links', views.familyLinks, name='family_links'),
    path('bible_engagements', views.bibleEngage, name='bible_engagements'),
    path('covid_relief', views.covidRelief, name='covid_relief'),
]
