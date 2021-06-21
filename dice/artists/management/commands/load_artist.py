import csv

from django.core.management import BaseCommand

from dice.artists.models import Artist


class Command(BaseCommand):
    help = "Load a artist csv file into the database"

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str)

    def handle(self, *args, **kwargs):
        path = kwargs["path"]
        with open(path, "rt") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                Artist.objects.create(
                    id=row[0], name=row[1], embedding=row[2], image_url=row[3]
                )
