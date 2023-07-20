# serializers.py

from rest_framework import serializers
from .models import Participantes

class ParticipanteSerial(serializers.ModelSerializer):
    class Meta:
        model = Participantes
        fields = '__all__'
