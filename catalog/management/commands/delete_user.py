from django.core.management.base import BaseCommand
from mainapp.models import User


class Command(BaseCommand):
    help = "Get all users"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            user.delete()
            self.stdout.write(f'Пользователь {user} с ID {pk} УДАЛЕН')
        else:
            self.stdout.write(f'Пользователь с ID {pk} не найден')
