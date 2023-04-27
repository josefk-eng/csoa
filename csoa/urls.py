from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('report',views.report, name='report'),
    path('about', include('whoweare.urls'))
]