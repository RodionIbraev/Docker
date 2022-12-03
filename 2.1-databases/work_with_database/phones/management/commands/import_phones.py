import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        for phone in phones:
            phone = Phone(id=phone["id"], name=phone["name"], image=phone["image"],
                price=phone["price"], release_date=phone["release_date"], lte_exist=phone["lte_exists"],
                slug='-'.join(phone['name'].split()))
            phone.save()