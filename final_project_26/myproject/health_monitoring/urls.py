from django.urls import path
from .views import patient_index

app_name = 'health_monitoring'

urlpatterns = [
    path('', patient_index, name='patient-index'),
]