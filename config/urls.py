from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^core/api/', include("apps.core.api.urls", namespace="core-api")),
    url(r'^', include_docs_urls(title='Work at OList Challenge')),
]
