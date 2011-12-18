from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.views.generic import TemplateView


# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'', TemplateView.as_view(template_name="pointing/run.html"), name="pointing"),
                       )


