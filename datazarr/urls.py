from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('u10/<str:latitude>/<str:longitude>/<str:time>', views.u10),
    path('v10/<str:latitude>/<str:longitude>/<str:time>', views.v10),
    path('t2m/<str:latitude>/<str:longitude>', views.t2m),
    path('anor/<str:latitude>/<str:longitude>', views.anor),
    path('isor/<str:latitude>/<str:longitude>', views.isor),
]
