from myblog.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
import uuid
import os
from django.core.files import File
from django.conf import settings
from django.http import Http404
from myforms import PostForm
from myforms import BlogForm
from myblog.models import Blog
from myblog.models import Tag
from myblog.models import Post
from myblog import constant
import html2text

import datetime
#import PyRSS2Gen
from django.contrib.syndication.views import Feed

class RssFeed(Feed):
    title = "Police beat site news"
    link = "/sitenews/"
    description = "Updates on changes and additions to police beat central."
    
    def get_object(self, request, blog_id=None):
        return Blog.objects.get(pk=blog_id)

    def title(self, obj):
        return obj.name

    def link(self, obj):
        return reverse('my_blogs_following_view', kwargs={'blog_id': obj.id})
        #return ''

    def description(self, obj):
        return obj.name

    def author_name(self, obj):
        return '%s %s' % (obj.creator.first_name, obj.creator.last_name )

    def author_email(self, obj):
        return obj.creator.email

    def items(self, obj):
        return Post.objects.filter(blog=obj) 

    def item_title(self, item):
        return item.title 

    def item_description(self, item):
        content = item.content
        content_plain_text = html2text.html2text(content)
        ret = content_plain_text[:constant.BRIEF_LENGTH]
        return ret 

    def item_link(self, item):
        return reverse('post_detail_embedded_view', kwargs={'post_id': item.id})

    def item_guid(self, item):
        return reverse('post_detail_embedded_view', kwargs={'post_id': item.id})

    def item_author_name(self, item):
        return '%s %s' % (item.author.first_name, item.author.last_name )

    def item_author_email(self, item):
        return item.author.email

    def item_pubdate(self, item):
        return item.create_time

def get_rss_interact(request, blog_id=None):
    blog = Blog.objects.get(pk=blog_id)
    title = blog.name

    link = reverse('post_detail_embedded_view', kwargs={'blog_id': blog_id} )
    description = title 
    items = []
        
    return HttpResponse(data_json, mimetype='application/json')
