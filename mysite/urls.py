from django.conf.urls import patterns, include, url
from django.contrib import admin
from Radar.views import *
from ScheduleTest.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^RadarWebServiceskeywords/', RadarWebServiceskeywords),
    url('^ScheduleTest/$', ScheduleTest),
    url('^welcome/$', RadarWebServiceswelcome),
    url(r'^RadarWebServicesprojectselect/', RadarWebServicesprojectselect),
    url(r'^RadarWebServices/', RadarWebServices),
    url(r'^$', RadarWebServices),
)