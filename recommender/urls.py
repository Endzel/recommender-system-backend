from django.conf.urls import url, include
from recommender.urls import api_urls

api_urls = [
    url(r'^api/', include(api_urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', AuthenticatedDRFDocsView.as_view(), name='drfdocs'),
]
