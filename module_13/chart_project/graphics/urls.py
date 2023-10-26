from django.urls import path
from . import views

urlpatterns = [
    path('temperature_chart/', views.temperature_chart, name='temperature_chart'),
]