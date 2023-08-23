import datetime

import requests
import soundcard
from django.core.management import BaseCommand


from kenguru.local_setting import CRM_CLIENT_SAVE_URL, MARKET_TOKEN, MARKET_CONNECT_STATUS
from kenguru.models import LocalSetting


class Command(BaseCommand):

    def handle(self, ip=None, *args, **options):
        """
        синхронизируеться с crm
        """
        try:
            local_setting = LocalSetting.objects.last()

            audio_list = soundcard.all_speakers()
            audio_list = list(map(lambda x: x.name, audio_list))

            try:
                ip = requests.get('https://api.ipify.org').content.decode('utf8')
            except Exception:
                ip = ''

            if local_setting.audio in audio_list:
                status = MARKET_CONNECT_STATUS.OK
            else:
                status = MARKET_CONNECT_STATUS.DONT_AUDIO

            requests.post(CRM_CLIENT_SAVE_URL, data={
                'token': MARKET_TOKEN,
                'ip': ip,
                'id': local_setting.market_id,
                'audio': local_setting.audio,
                'status': status
            })

            self.stdout.write(self.style.SUCCESS(f'Клиент синхронизировался'))
        except Exception:
            self.stdout.write(self.style.SUCCESS(f'Клиент ещё нe настроен'))


