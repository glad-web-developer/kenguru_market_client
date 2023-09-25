import requests

from kenguru.local_setting import CRM_CLIENT_SAVE_URL, MARKET_TOKEN, MARKET_CONNECT_STATUS
from kenguru.models import LocalSetting


class ClientService:
    def send_to_crm(self):
        local_setting = LocalSetting.objects.last()

        status = MARKET_CONNECT_STATUS.DONT_AUDIO
        # todo
        status = MARKET_CONNECT_STATUS.OK



        requests.post(CRM_CLIENT_SAVE_URL, data={
            'token': MARKET_TOKEN,
            'id': local_setting.market_id,
            'status': status
        })