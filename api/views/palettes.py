from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.palette import PaletteSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..models.palette import Palette

class PalettesView(APIView):
    def post(self, request):
        palette = PaletteSerializer(data=request.data)
        if palette.is_valid():
            palette.save()
            return Response(palette.data, status=status.HTTP_201_CREATED)
        else:
            return Response(palette.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self):
        palettes = Palette.objects.all()
        data = PaletteSerializer(palettes, many=True).data
        return Response(data)