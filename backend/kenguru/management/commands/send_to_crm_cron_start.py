import time

from django.core.management import BaseCommand

from kenguru.local_setting import SYNC_TYME_SEC
from kenguru.services import ClientService


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        синхронизируеться с crm
        """
        while True:
            try:
                service = ClientService()
                service.send_to_crm()
                self.stdout.write(self.style.SUCCESS(f'Клиент синхронизировался'))
            except Exception:
                self.stdout.write(self.style.SUCCESS(f'Клиент ещё нe настроен'))

            time.sleep(SYNC_TYME_SEC)


