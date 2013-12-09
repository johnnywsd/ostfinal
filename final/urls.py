from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static
from myblog.rss import RssFeed

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
    url(r'^my_blogs$', 'myblog.views.my_blogs_view', name='my_blogs_view'),
    url(r'^test_page$', 'myblog.views.test_page_view', name='test_page'),
    url(r'^my_blogs/', include('final.my_blogs_urls')),

    url(r'^get_users_ajax$', 'myblog.interacts.get_users_ajax',
        name='get_users_ajax'),
    url(r'^get_users_by_ids_ajax$', 'myblog.interacts.get_users_by_ids_ajax',
        name='get_users_by_ids_ajax'),

    url(r'^rss/(?P<blog_id>\d+)/$', RssFeed(),
        name='rss'),

    url(r'^latest_post_list/$', 'myblog.views.latest_post_list_view',
        name='latest_post_list_view'),

    url(r'^tag_post_list/(?P<tag_id>\d+)/$', 'myblog.views.tag_post_list_view',
        name='tag_post_list_view'),
    url(r'^tag_post_list/(?P<tag_id>\d+)/(?P<blog_ids>[0-9,]*)/$',
        'myblog.views.tag_post_list_view',
        name='tag_post_list_view'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
