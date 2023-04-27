from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.overview, name='overview'),
    path('examination', views.examination, name='examination'),
    path('academic_seminars', views.seminars, name='academic_seminars'),
    path('awareness_climate_conservation', views.awarenessClimate, name='awareness_climate_conservation'),
    path('awareness_children_in_school', views.childrenInSchool, name='awareness_children_in_school'),
    path('boy_child_awakening', views.boyChild, name='boy_child_awakening'),
    path('discipleship', views.discipleship, name='discipleship'),
    path('girl_child_emp', views.girlChild, name='girl_child_emp'),
    path('menstrual', views.menstrual, name='menstrual'),
    path('prayer_networks', views.prayerNet, name='prayer_networks'),
    path('regionalMDD', views.regionalMDD, name='regionalMDD'),
    path('regionalSportsGalour', views.regionalSportsGalour, name='regionalSportsGalour'),
]
