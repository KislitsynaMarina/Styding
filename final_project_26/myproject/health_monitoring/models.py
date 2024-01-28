from django.db import models


class PatientInfo(models.Model):
    age = models.IntegerField(default=0)
    gender = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    weight = models.FloatField(default=0)
    ap_hi = models.IntegerField(default=0)
    ap_lo = models.IntegerField(default=0)
    cholesterol = models.IntegerField(default=0)
    gluc = models.IntegerField(default=0)
    smoke = models.IntegerField(default=0)
    alco = models.IntegerField(default=0)
    active = models.IntegerField(default=0)
    cardio = models.IntegerField(default=0)