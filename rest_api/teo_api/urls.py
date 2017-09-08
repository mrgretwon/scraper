from django.conf.urls import url
from teo_api import views

urlpatterns = [
    url(r'^stats/$', views.Stats.as_view(), name = "stats"),
    url(r'^stats/(?P<req>\w+)/$', views.Author.as_view(), name = "author")]
