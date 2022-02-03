from rest_framework import serializers
from ..models.palette import Palette

class PaletteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palette
        fields = '__all__'