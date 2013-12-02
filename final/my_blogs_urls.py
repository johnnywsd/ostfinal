from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^own$',
        'myblog.my_blogs_views.my_blogs_own_view',
        name='my_blogs_own_view'),

    url(r'^own/(?P<blog_id>\d+)$',
        'myblog.my_blogs_views.my_blogs_own_view',
        name='my_blogs_own_view'),

    url(r'^shared$',
        'myblog.my_blogs_views.my_blogs_shared_view',
        name='my_blogs_shared_view'),

    url(r'^shared/(?P<blog_id>\d+)$',
        'myblog.my_blogs_views.my_blogs_shared_view',
        name='my_blogs_shared_view'),

    url(r'^following$',
        'myblog.my_blogs_views.my_blogs_following_view',
        name='my_blogs_following_view'),

    url(r'^following/(?P<blog_id>\d+)$',
        'myblog.my_blogs_views.my_blogs_following_view',
        name='my_blogs_following_view'),

    url(r'^post_detail/(?P<post_id>\d+)$',
        'myblog.my_blogs_views.post_detail_embedded_view',
        name='post_detail_embedded_view'),
)