import datetime
from django.core.management.base import BaseCommand
from mainapp.models import User


class Command(BaseCommand):
    help = "Create user"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Username')
        parser.add_argument('email', type=str, help='Email')
        parser.add_argument('phone', type=str, help='Phone')
        parser.add_argument('address', type=str, help='Address')


    def handle(self, *args, **kwargs):
        # Работа через параметры
        name = kwargs['name']
        email = kwargs['email']
        phone = kwargs['phone']
        address = kwargs['address']
        # Работа через консоль без параметров
        # name = input("Имя пользователя: ")
        # email = input("Email (Формат: name@mail.ru): ")
        # phone = input("Номер телефона: ")
        # address = input("Адрес: ")
        date = datetime.datetime.now()
        user = User(name=name, email=email, phone=phone, address=address,
                    date_registration=date)

        user.save()
        self.stdout.write(f'{user}')
