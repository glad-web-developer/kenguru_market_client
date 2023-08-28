from kenguru.local_setting import CRM_CLIENT_SAVE_URL, MARKET_TOKEN, MARKET_CONNECT_STATUS
from kenguru.models import LocalSetting


import requests
import soundcard

class ClientService:
    def send_to_crm(self):
        local_setting = LocalSetting.objects.last()

        audio_list = soundcard.all_speakers()
        audio_list = list(map(lambda x: x.name, audio_list))

        if local_setting.audio in audio_list:
            status = MARKET_CONNECT_STATUS.OK
        else:
            status = MARKET_CONNECT_STATUS.DONT_AUDIO

        requests.post(CRM_CLIENT_SAVE_URL, data={
            'token': MARKET_TOKEN,
            'id': local_setting.market_id,
            'audio': local_setting.audio,
            'status': status
        })