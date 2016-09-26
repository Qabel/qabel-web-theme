
from django.conf.urls import include, url, i18n

urlpatterns = [
    url(r'^i18n/', include(i18n)),
]
