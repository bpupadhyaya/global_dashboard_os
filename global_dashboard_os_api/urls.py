from django.urls import path
from .views import IncidentView

urlpatterns = [
    path('incident', IncidentView.as_view()),
]