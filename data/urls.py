from django.urls import path
from .views import VisualizationView


urlpatterns = [
    path('getall/',VisualizationView.as_view(),name='visualization')
]
