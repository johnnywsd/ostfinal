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

    url(r'^post_edit/$',
        'myblog.my_blogs_views.post_edit_embedded_view',
        name='post_edit_embedded_view'),

    url(r'^post_add/(?P<blog_id>\d+)$',
        'myblog.my_blogs_views.post_edit_embedded_view',
        name='post_add_embedded_view'),

    url(r'^post_edit/(?P<post_id>\d+)$',
        'myblog.my_blogs_views.post_edit_embedded_view',
        name='post_edit_embedded_view'),

    url(r'^post_edit/(?P<blog_id>\d+)/(?P<post_id>\d+)$',
        'myblog.my_blogs_views.post_edit_embedded_view',
        name='post_edit_embedded_view'),

    url(r'^post_edit_interact$',
        'myblog.interacts_my_blogs.post_edit_interact',
        name='post_edit_interact'),

    url(r'^post_edit_interact/(?P<post_id>\d+)$',
        'myblog.interacts_my_blogs.post_edit_interact',
        name='post_edit_interact'),

    url(r'^post_edit_interact/(?P<blog_id>\d+)/(?P<post_id>\d+)/$',
        'myblog.interacts_my_blogs.post_edit_interact',
        name='post_edit_interact'),

    url(r'^post_delete_interact/(?P<post_id>\d+)/$',
        'myblog.interacts_my_blogs.post_delete_interact',
        name='post_delete_interact'),

    url(r'^blog_edit_interact/$',
        'myblog.interacts_my_blogs.blog_edit_interact',
        name='blog_edit_interact'),

    url(r'^blog_delete_interact/(?P<blog_id>\d+)/$',
        'myblog.interacts_my_blogs.blog_delete_interact',
        name='blog_delete_interact'),

    url(r'^blog_revoke_interact/(?P<blog_id>\d+)/$',
        'myblog.interacts_my_blogs.blog_revoke_interact',
        name='blog_revoke_interact'),

    #url(r'^image_upload_interact/$',
        #'myblog.interacts_file.img_upload_interact',
        #name='image_upload_interact'),
)
