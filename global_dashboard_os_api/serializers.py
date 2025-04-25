from rest_framework import serializers
from .models import Incident


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = (
            'id',  # Added for unique model identification
            'incident_number',
            'state',
            'caller',
            'owned_by',
            'contact_type',
            'due_date',
            # TODO
            'configuration_item',
            # TODO
            'environment',
            # TODO
            'assignment_group',
            'assigned_to',
            'technical_dri',
            'title',
            'description'
            # TODO
        )