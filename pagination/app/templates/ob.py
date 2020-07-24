import csv

# знаю что надо использовать django.conf но почему то не работает
from app import settings

CONTENT = []
with open(settings.BUS_STATION_CSV, encoding='cp1251') as csvfile:
    reader = csv.DictReader(csvfile)
    with open(settings.BUS_STATION_CSV, encoding='cp1251') as csvfile:
        reader = csv.DictReader(csvfile)
        for element in reader:
            CONTENT.append({"Name" : element["Name"], "Street" : element["Street"], "AdmArea" : element["AdmArea"]})

print(CONTENT[1])