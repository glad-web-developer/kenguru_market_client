from django.db import models
from kenguru.local_setting import MARKET_CONNECT_STATUS


class LocalSetting(models.Model):
    class Meta:
        verbose_name = 'Локальные настройки'
        verbose_name_plural = 'Локальные настройки'

    market_id = models.IntegerField('Маркет ID',)
    market_name = models.CharField('Маркет', max_length=255)
    connect_status = models.IntegerField('Статус клиента', choices=MARKET_CONNECT_STATUS.choices,
                                         default=MARKET_CONNECT_STATUS.DONT_FIRST_CONNECT)
    date_update = models.DateTimeField('Дата обновления', auto_now=True)