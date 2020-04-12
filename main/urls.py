from django.conf.urls import url

from . import views
# import views so we can use them in urls.py.

app_name = 'main'

# Sentry test
def trigger_error(request):
        division_by_zero = 1 / 0

urlpatterns = [
    url(r'^sentry-debug/$', trigger_error),
    url(r'^$', views.index_view, name="index"),
    url(r'^mentions/$', views.mentions_view, name="mentions"),
]
