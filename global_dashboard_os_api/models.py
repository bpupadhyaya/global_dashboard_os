from datetime import datetime
from django.db import models

# Create your models here.


class Incident(models.Model):
    incident_number = models.CharField(max_length=20, default="", unique=True)
    state = models.CharField(max_length=40, default="Escalate", unique=False)
    caller = models.CharField(max_length=50, default="", unique=False)
    owned_by = models.CharField(max_length=50, default="", unique=False)
    contact_type = models.CharField(max_length=40, default="", unique=False)
    due_date = models.DateField(default=datetime.today(), unique=False)
    # TODO
    configuration_item = models.CharField(max_length=60, default="", unique=False)
    # TODO
    environment = models.CharField(max_length=30, default="", unique=False)
    # TODO
    assignment_group = models.CharField(max_length=70, default="", unique=False)
    assigned_to = models.CharField(max_length=50, default="", unique=False)
    technical_dri = models.CharField(max_length=50, default="", unique=False)
    title = models.CharField(max_length=100, default="", unique=False)
    description = models.CharField(max_length=500, default="", unique=False)
    # TODO