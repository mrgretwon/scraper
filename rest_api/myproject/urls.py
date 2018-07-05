from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Blog API')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^', include('teo_api.urls')),
]
