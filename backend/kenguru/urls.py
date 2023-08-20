from django.conf import settings
from django.contrib import admin

from django.urls import path
from django.conf.urls.static import static
from django.views.generic import TemplateView

from kenguru.api import LocalSettingApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_local_setting', LocalSettingApi.as_view()),
    path('', TemplateView.as_view(template_name="index.html"))

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
