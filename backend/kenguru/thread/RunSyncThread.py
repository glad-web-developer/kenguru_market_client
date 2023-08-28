import time
from threading import Thread

from kenguru.local_setting import SYNC_TYME_SEC
from kenguru.services.ClientService import ClientService
import datetime

class RunSyncThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.running = True
        self.service = ClientService()

    def run(self):
        while self.running:
            try:
                self.service.send_to_crm()
                print(f'{datetime.datetime.now()} - Данные отправились в CRM')
            except Exception as e:
                print(f'{datetime.datetime.now()} - Ошибка отправки в CRM {e}')
            time.sleep(SYNC_TYME_SEC)

    def stop(self):
        self.running = False