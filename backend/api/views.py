from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DisorderSerializer
from .models import Disorder


# Create your views here.

# Get all disorders
class DisorderView(viewsets.ModelViewSet):
    serializer_class = DisorderSerializer
    queryset = Disorder.objects.all()

class DisorderView(viewsets.ModelViewSet):
    serializer_class = DisorderSerializer
    ##    Author.objects.all()
    queryset = Disorder.objects.filter(symptoms__contains=["HP:0008765"])