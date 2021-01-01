from django.urls import path

from . import views
from .dash import flood_graph

urlpatterns = [
    path('', views.dashboard, name='main_dash'),
]