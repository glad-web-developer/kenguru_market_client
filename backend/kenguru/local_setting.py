import os
from django.db import models

from kenguru.settings import BASE_DIR
# BASE_URL = 'http://127.0.0.1:8000'
BASE_URL = 'http://crm.ikenguru.ru'
SECRET_KEY = 'django-insecure-%(k0$a0y6!j+(kptj*=tn^_=&!4x_7e3$xyjyp$=xc1b0+^pv+'
CORS_ORIGIN_WHITELIST = ["http://localhost:8080", 'http://crm.ikenguru.ru', 'http://localhost:127.0.0.1']


MEDIA_ROOT = os.path.join(BASE_DIR,'media')
STATIC_ROOT = os.path.join(BASE_DIR,'static')

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':  'db.sqlite3',
    },
}


class MARKET_CONNECT_STATUS(models.IntegerChoices):
    DONT_FIRST_CONNECT = 1, 'Не было первичного подключения от клиента'
    DONT_SETTING_AUDIO = 2, 'Не указаны настройки аудио девайса на клиенте'
    OK = 3, 'Всё работает'
    DONT_CONNECT = 4, 'Нет подключения по сети'
    DONT_AUDIO = 5, 'Не найдено звуковое устройство'

MARKET_TOKEN = '!!!ken!!!guru!!'
CRM_CLIENT_SAVE_URL = f'{BASE_URL}/api1/market/client_save'


