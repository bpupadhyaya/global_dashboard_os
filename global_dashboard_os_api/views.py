from rest_framework import generics
from .models import Incident
from .serializers import IncidentSerializer


# Create your views here.
class IncidentView(generics.CreateAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer





