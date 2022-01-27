from django.urls import path
from . import views

app_name = 'EdgarWebsite'

urlpatterns = [
    path("", views.home, name="home"),
    path("cover", views.cover, name="cover"),
    path("resume", views.resume, name="resume"),
]