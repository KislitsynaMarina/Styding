from django.contrib import admin
from .models import PatientInfo


class PatientInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'age', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio']


admin.site.register(PatientInfo, PatientInfoAdmin)