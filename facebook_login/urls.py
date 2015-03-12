from django.conf.urls import patterns, url
from facebook_login import views

urlpatterns = patterns('',
    url(r'^login/$', 'facebook_login.views.login', name='login_page'),
    url(r'^login_success/', 'facebook_login.views.login_success', name='login_success_page')
    )
