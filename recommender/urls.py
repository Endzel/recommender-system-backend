from django.conf.urls import url, include
from django.contrib import admin
from drfdocs.views import AuthenticatedDRFDocsView

api_urls = []

urlpatterns = [
    url(r'^api/', include(api_urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', AuthenticatedDRFDocsView.as_view(), name='drfdocs'),
]
