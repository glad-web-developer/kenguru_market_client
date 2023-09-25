from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from kenguru.models import LocalSetting
from kenguru.serializers import LocalSettingSerializer
from kenguru.services import ClientService


class LocalSettingApi(APIView):
    def get(self, request):

        try:
            local_setting = LocalSetting.objects.last()
        except Exception:
            local_setting = LocalSetting()

        serializer = LocalSettingSerializer(local_setting, many=False)
        return Response({
            'setting':serializer.data,
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


        service = ClientService()
        r = service.send_to_crm()

        if r.status_code == 200:
            return Response({'status':'ok'})
        return HttpResponse(r.text, status=400)



