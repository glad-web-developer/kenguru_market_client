from rest_framework import serializers

from kenguru.models import LocalSetting


class LocalSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalSetting
        fields = '__all__'

    date_update = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S', required=False)