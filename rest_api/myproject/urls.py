from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('teo_api.urls')),
]
