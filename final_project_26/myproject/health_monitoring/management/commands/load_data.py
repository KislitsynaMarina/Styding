import csv
from inspect import Traceback
from sqlite3 import IntegrityError

from django.core.management.base import BaseCommand

from ...models import PatientInfo


class Command(BaseCommand):
    def handle(self, *args, **options):
        temp_data = []
        with open('medical_examination.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            next(reader)
            count = 0
            for row in reader:
                count += 1
                if PatientInfo.objects.filter(id=row[0]).exists():
                    print(f'patient with id={row[0]} already exists!')
                else:
                    temp_data.append(PatientInfo(
                        id=row[0],
                        age=row[1],
                        gender=row[2],
                        height=row[3],
                        weight=row[4],
                        ap_hi=row[5],
                        ap_lo=row[6],
                        cholesterol=row[7],
                        gluc=row[8],
                        smoke=row[9],
                        alco=row[10],
                        active=row[11],
                        cardio=row[12],
                    ))
                    print(f'object_created {count}')

        print('start bulk_create')
        PatientInfo.objects.bulk_create(temp_data, batch_size=999)
        print('finish bulk_create')

