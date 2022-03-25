from rest_framework import serializers
from .models import Disease

class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ('orpha_code', 'name', 'symptoms')

class InputParameterSerializer(serializers.Serializer):
    label = serializers.CharField()
    value = serializers.CharField()