from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()

        categories_list = []
        categories = [{'name': 'some', 'info': 'news'}]

        for item in categories:
            categories_list.append(
                Category(**item)
            )

        Category.objects.bulk_create(categories_list)