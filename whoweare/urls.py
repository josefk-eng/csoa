from django.urls import path
from . import views

urlpatterns = [
    path('',views.statements, name='statements'),
    path('network',views.network, name='network'),
    path('history',views.history, name='history'),
    path('partners',views.partners, name='partners'),
    path('modeofoperation',views.modeofoperation, name='modeofoperation'),
    path('portfolios',views.portfolios, name='portfolios'),
]