from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hightolowrate', views.hightolowrate, name='hightolowrate'),
    path('hightolow', views.hightolow, name='hightolow'),
    path('lowtohigh', views.lowtohigh, name='lowtohigh'),



]
