import os.path
import subprocess

import requests

from kenguru.local_setting import CRM_CLIENT_SAVE_URL, MARKET_TOKEN, MARKET_CONNECT_STATUS
from kenguru.models import LocalSetting
from kenguru.settings import BASE_DIR


class ClientService:
    def send_to_crm(self):
        local_setting = LocalSetting.objects.last()

        status = MARKET_CONNECT_STATUS.DONT_AUDIO
        try:
            path = os.path.join(BASE_DIR,'С#', 'kenguru.exe')
            proc = subprocess.run(path, stdout=subprocess.PIPE, text=True)
            volume = proc.stdout
            for i in volume:
                try:
                    if ',' in i:
                        i = i.replace(',', '.')

                    if float(i) > 0.001:
                        status = MARKET_CONNECT_STATUS.OK
                except Exception:
                    pass

        except Exception as e:
            print('Ошибка с C# ' + str(e))


        return requests.post(CRM_CLIENT_SAVE_URL, data={
            'token': MARKET_TOKEN,
            'id': local_setting.market_id,
            'status': status
        })