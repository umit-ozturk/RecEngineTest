import csv

from django.core.management import BaseCommand

from dice.users.models import User


class Command(BaseCommand):
    help = "Load a user csv file into the database"

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str)

    def handle(self, *args, **kwargs):
        path = kwargs["path"]
        with open(path, "rt") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                print(row)
                User.objects.create(
                    id=row[0],
                    username=row[0],  # Username is same with user_id.
                    password="dice_exercise",
                    embedding=row[1],
                )
