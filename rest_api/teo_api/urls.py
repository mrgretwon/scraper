from django.conf.urls import url
from teo_api import views

urlpatterns = [
    url(r'^stats/$', views.Stats.as_view()),
    url(r'^stats/(?P<cos>\w+)/$', views.Author.as_view())]
