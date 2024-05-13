
from datetime import timedelta
from django.core.management.base import BaseCommand
from catalog.models import Product


class Command(BaseCommand):
    help = "Get all users"

    def handle(self, *args, **options):
        users = Product.objects.all()
        for user in users:
            self.time = timedelta(0)
            user.save()
            