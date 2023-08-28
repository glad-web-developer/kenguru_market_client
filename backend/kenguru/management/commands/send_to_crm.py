
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
            self.stdout.write(self.style.SUCCESS(f'Клиент синхронизировался'))
        except Exception:
            self.stdout.write(self.style.SUCCESS(f'Клиент ещё нe настроен'))


