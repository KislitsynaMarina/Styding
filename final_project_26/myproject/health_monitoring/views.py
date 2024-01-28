from django.http import HttpRequest
from django.shortcuts import render
from .models import PatientInfo


def patient_index(request: HttpRequest):
    patient = PatientInfo.objects.all()

    return render(request, 'health_monitoring/patient-index.html', {'patient': patient})
