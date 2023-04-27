from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.prayer, name='prayer'),
    path('stories', views.stories, name='stories'),
    path('partnership', views.partnership, name='partnership'),
    path('what_they_say', views.testimonial, name='what_they_say'),
    path('news', views.news, name='news'),
]
