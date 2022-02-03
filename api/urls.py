#api/urls.py

from django.urls import path
from .views import palettes

urlpatterns = [
    path('palettes/', palettes.PalettesView.as_view(), name='index'),
    path('palettes/<int:id>/', palettes.PalettesView.as_view(), name='Palette-detail')
]