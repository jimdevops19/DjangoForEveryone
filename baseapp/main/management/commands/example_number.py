from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Display some number you'd like to display"

    def add_arguments(self, parser):
        parser.add_argument('my_num', type=int)

    def handle(self, *args, **options):
        print(f"The number was {options.get('my_num')}")
