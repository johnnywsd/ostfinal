from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'final.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index$', 'myblog.views.home_view', name='home'),
    url(r'^sign_up$', 'myblog.views.sign_up_view', name='sign_up'),
    url(r'^sign_up_interact$', 'myblog.interacts.sign_up_interact', name='sign_up_interact'),
    url(r'^about$', 'myblog.views.about_view', name='about'),
    url(r'^login$', 'myblog.views.login_view', name='login'),

    url(r'^login_interact$', 'myblog.interacts.login_user', name='login_interact'),
    url(r'^logout$', 'myblog.interacts.logout_user', name='logout'),

)
