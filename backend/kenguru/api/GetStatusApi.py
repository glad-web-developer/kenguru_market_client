import soundcard
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import requests

from kenguru.local_setting import CRM_CLIENT_SAVE_URL, MARKET_TOKEN
from kenguru.models import LocalSetting
from kenguru.serializers import LocalSettingSerializer


class GetStatusApi(APIView):
    def get(self, request):
        """
        когда стучаться из вне поверят что есть звук
        """

        try:
            local_setting = LocalSetting.objects.last()
            audio_list = soundcard.all_speakers()
            audio_list = list(map(lambda x: x.name, audio_list))
            if local_setting.audio in audio_list:
                return Response("ok")
            return Response("Нет устройства")
        except Exception:
            return Response("Не настроен клиент")





