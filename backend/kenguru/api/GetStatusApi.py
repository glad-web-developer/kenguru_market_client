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

        try:
            local_setting = LocalSetting.objects.last()
        except Exception:
            local_setting = LocalSetting()


        audio_list = soundcard.all_speakers()
        audio_list = list(map(lambda x : x.name, audio_list))
        audio = request.query_params['audio']
        if audio in audio_list:
            return Response("ok")
        else:
            return Response("Нет устройства")




