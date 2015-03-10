from django.conf.urls import patterns, url
from facebook_login import views

urlpatterns = patterns('',
    url(r'^login/$', 'facebook_login.views.login'),
    url(r'^login_success/', 'facebook_login.views.login_success')
    )
