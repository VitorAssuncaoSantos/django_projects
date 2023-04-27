from django.contrib import admin
from django.urls import path
from . import views

app_name = "chat_pmnf"
urlpatterns = [
    path("", views.index, name="index"),
     path("sala/<id>", views.sala, name="sala"),
    path("mensagens/<sala>", views.get_mensagens, name = "get_mensagens")
]
