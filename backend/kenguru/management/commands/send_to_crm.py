import datetime

from django.core.management import BaseCommand

from kenguru.services import ClientService


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        синхронизируеться с crm
        """
        try:
            service = ClientService()
            service.send_to_crm()
            self.stdout.write(self.style.SUCCESS(f'{datetime.datetime.now()} Клиент синхронизировался'))
        except Exception:
            self.stdout.write(self.style.SUCCESS(f'{datetime.datetime.now()} Клиент ещё нe настроен'))


