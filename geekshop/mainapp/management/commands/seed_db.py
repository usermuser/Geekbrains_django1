from django.core.management.base import BaseCommand

from mainapp.models import Category



class Command(BaseCommand):
    def handle(self, *args, **options):

        Category.objects.all().delete()

        for x in range(5):
            new_cat = Category()
            new_cat.save()