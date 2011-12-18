from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.views.generic import TemplateView


# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', TemplateView.as_view(template_name="index.html")),
                       url(r'^about$', TemplateView.as_view(template_name="about.html")),
                       url(r'^logout$', logout, name="logout"),
                       url(r'^login$', login, name="login"),
                       url(r'^accounts/', include('accounts.urls')),
                       url(r'^writing/', include('writing.urls')),
                       url(r'^reading/', include('reading.urls')),
                       url(r'^pointing/', include('pointing.urls')),
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )

