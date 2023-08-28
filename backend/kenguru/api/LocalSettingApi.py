import soundcard
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import requests

from kenguru.local_setting import CRM_CLIENT_SAVE_URL, MARKET_TOKEN, MARKET_CONNECT_STATUS
from kenguru.models import LocalSetting
from kenguru.serializers import LocalSettingSerializer


class LocalSettingApi(APIView):
    def get(self, request):

        try:
            local_setting = LocalSetting.objects.last()
        except Exception:
            local_setting = LocalSetting()



        serializer = LocalSettingSerializer(local_setting, many=False)
        audio_list = soundcard.all_speakers()
        audio_list = list(map(lambda x : x.name, audio_list))
        return Response({
            'setting':serializer.data,
            'audio_list':audio_list,
        })

    def post(self, request):
        try:
            ls = LocalSetting.objects.last()
            serializer = LocalSettingSerializer(ls, data=request.data)
        except Exception:
            serializer = LocalSettingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        r = requests.post(CRM_CLIENT_SAVE_URL, data={
            'token':MARKET_TOKEN,
            'status': MARKET_CONNECT_STATUS.OK,
            'audio': request.data['audio'],
            'id':request.data['market_id'],
        })

        return Response({'status':'ok'})



