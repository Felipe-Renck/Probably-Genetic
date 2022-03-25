from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DiseaseSerializer, InputParameterSerializer
from .models import Disease

class DiseaseViews(APIView):

    def get(self, request, id=None):
        if id:
            item = Disease.objects.get(id=id)
            serializer = DiseaseSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Disease.objects.all()
        serializer = DiseaseSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = InputParameterSerializer(data=request.data, many=True)
        if serializer.is_valid():
            hpo_list = []
            for hpo_item in serializer.data:
                hpo_id = str(list(hpo_item.items())[0][1])
                hpo_list.append(hpo_id)

            items = Disease.objects.filter(symptoms__contains=hpo_list)
            serializer = DiseaseSerializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
