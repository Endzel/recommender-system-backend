from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import re_path
from django.views.static import serve

from recommender.urls import api_urls

urlpatterns = [
    url(r'^api/', include(api_urls)),
    url(r'^admin/', admin.site.urls),

    # Media
    re_path(r'^(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
            }),
]
