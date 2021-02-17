from django.urls import path
from . import views

urlpatterns = [
    path("", views.root),
    path("survey_complete", views.survey_complete),
    path("result", views.result),
]