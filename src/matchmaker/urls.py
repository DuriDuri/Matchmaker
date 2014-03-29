from django.conf.urls import patterns, include, url
from django.conf import settings


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.default.urls')),
    url(r'^edit/$', 'profiles.views.edit_profile', name = 'edit_profile'),
    url(r'^$', 'profiles.views.all', name = 'Home'),
    url(r'^members/(?P<username>\w+)/$', 'profiles.views.single_user'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    
)
