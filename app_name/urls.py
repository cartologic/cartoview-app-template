from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from . import views, APP_NAME

urlpatterns = patterns('',
   # app urls
   url(r'^$', views.index, name='%s.index' % APP_NAME),

)
