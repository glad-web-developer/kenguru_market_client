import datetime
import threading
import time

from django.conf import settings
from django.contrib import admin

from django.urls import path
from django.conf.urls.static import static
from django.views.generic import TemplateView

from kenguru.api import LocalSettingApi
from kenguru.thread import RunSyncThread

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_local_setting', LocalSettingApi.as_view()),
    path('', TemplateView.as_view(template_name="index.html"))

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# запуск синхронизации каждые 10(по умолчанию) секунд
sync_thread = RunSyncThread()
sync_thread.start()


# import sounddevice as sd
#
# duration = 10  # seconds
#
# def print_sound(indata, outdata, frames, time, status):
#     print (indata)
#
# while True:
#     with sd.Stream(callback=print_sound):
#         sd.sleep(duration * 1000)

# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
# devices = AudioUtilities.GetSpeakers()
# interface = devices.Activate(
#     IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = interface.QueryInterface(IAudioEndpointVolume)
# volume.GetMute()
# volume.GetMasterVolumeLevel()
# volume.GetVolumeRange()