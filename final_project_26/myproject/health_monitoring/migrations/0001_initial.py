# Generated by Django 4.2.6 on 2024-01-28 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=0)),
                ('gender', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('weight', models.FloatField(default=0)),
                ('ap_hi', models.IntegerField(default=0)),
                ('ap_lo', models.IntegerField(default=0)),
                ('cholesterol', models.IntegerField(default=0)),
                ('gluc', models.IntegerField(default=0)),
                ('smoke', models.IntegerField(default=0)),
                ('alco', models.IntegerField(default=0)),
                ('active', models.IntegerField(default=0)),
                ('cardio', models.IntegerField(default=0)),
            ],
        ),
    ]
