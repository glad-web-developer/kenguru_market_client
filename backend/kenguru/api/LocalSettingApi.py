import soundcard
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from kenguru.models import LocalSetting
from kenguru.serializers import LocalSettingSerializer


class LocalSettingApi(APIView):
    def get(self, request):

        try:
            local_setting = LocalSetting.objects.last()
        except Exception:
            local_setting = LocalSetting()

        try:
            ip = requests.get('https://api.ipify.org').content.decode('utf8')
        except Exception:
            raise Exception('Не смог получить IP клиента от сайта https://api.ipify.org')


        serializer = LocalSettingSerializer(local_setting, many=False)
        audio_list = soundcard.all_speakers()
        audio_list = list(map(lambda x : x.name, audio_list))
        return Response({
            'setting':serializer.data,
            'audio_list':audio_list,
            'ip':ip,
        })

    def post(self, request):
        try:
            ls = LocalSetting.objects.last()
            serializer = LocalSettingSerializer(ls, data=request.data)
        except Exception:
            serializer = LocalSettingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


