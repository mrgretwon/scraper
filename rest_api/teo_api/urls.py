from django.conf.urls import url
from teo_api import views

urlpatterns = [
    url(r'^authors/$', views.AuthorsListView.as_view(), name="list"),
    url(r'^stats/$', views.StatsView.as_view(), name="stats"),
    url(r'^stats/(?P<req>\w+)/$', views.AuthorView.as_view(), name="author")]
