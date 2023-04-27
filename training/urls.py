from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.leadership, name='leadership'),
    path('mgt_training', views.schoolMgt, name='mgt_training'),
    path('itAndAuto', views.itAndAuto, name='itAndAuto'),
    path('literacy', views.financialLiteracy, name='literacy'),
    path('capacity', views.capacityBuilding, name='capacity'),
]
