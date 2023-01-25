from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()

        categories_list = []
        categories = [
            {'name': 'Fruits ', 'info': 'the part of a plant that consists of one or more seeds and a soft inner part, can be eaten as food and usually tastes sweet'},
            {'name': 'Vegetables ', 'info': 'a plant or part of a plant that is eaten as food'},
            {'name': 'Canned Goods ', 'info': 'preserved in a can'},
            {'name': 'Dairy ', 'info': 'milk, cheese and other milk products'},
            {'name': 'Meat', 'info': 'the soft part of an animal or a bird that can be eaten as food'},
            {'name': 'Fish & Seafood', 'info': 'fish and sea creatures that can be eaten, especially shellfish'},
            {'name': 'Deli— Cheese', 'info': 'a shop or part of one that sells cooked meats and cheeses, and special or unusual foods that come from other countries'},
            {'name': 'Condiments & Spices', 'info': 'a substance such as salt, pepper or a sauce that is added to food to give it extra taste'},
            {'name': 'Snacks', 'info': 'a small meal or amount of food, usually eaten in a hurry'},
            {'name': 'Bread & Bakery', 'info': 'a type of food made from flour, water and usually yeast mixed together and baked'},
            {'name': 'Beverages— Coffee', 'info': 'any type of drink except water'},
            {'name': 'Pasta, Rice & Cereal—Oats', 'info': 'an Italian food made from flour, water and sometimes eggs, formed into different shapes and usually served with a sauce'},
            {'name': 'Baking— Flour', 'info': 'flour that does not contain baking powder'},
            {'name': 'Frozen Foods', 'info': 'food kept at a very low temperature in order to preserve it'},
            {'name': 'Personal Care', 'info': 'products help caring for somebody/something and providing what they need for their health or protection'},
            {'name': 'Health Care', 'info': ' a substance used as a medicine or used in a medicine'},
            {'name': 'Household & Cleaning Supplies', 'info': 'something that helps remove the dirt or dust from something'},
            {'name': 'Baby Items', 'info': ' to lose something that you want at the same time as you are trying to get rid of something that you do not want'},
            {'name': 'Pet Care', 'info': 'a person who is given special attention by somebody, especially in a way that seems unfair to other people'},
        ]

        for item in categories:
            categories_list.append(
                Category(**item)
            )

        Category.objects.bulk_create(categories_list)