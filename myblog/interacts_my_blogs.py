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
from myblog.models import Blog
from myblog.models import Tag


@login_required
def post_edit_interact(request, blog_id=None, post_id=None):
    user = request.user
    #return HttpResponse(post_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            #post_id = form.cleaned_data['post_id']
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            tags_str = form.cleaned_data['tags']
            tag_names = tags_str.split(',')
            tags = Tag.objects.filter(name__in=tag_names)
            if post_id:
                post = Post.objects.get(pk=post_id)
            else:
                post = Post()

            blog_id = form.cleaned_data['blog_id']
            if blog_id:
                post.blog = Blog.objects.get(pk=blog_id)
            post.title = title
            post.content = content
            post.author = user
            post.save()
            post.tags = tags
            post.save()

            nextUrl = reverse('post_detail_embedded_view', 
                            kwargs={'post_id': str(post.id)}
                            )

            return HttpResponseRedirect(nextUrl)

            #return HttpResponse(tags)
            #return HttpResponse(title+content+"<br>"+tags_str)
        

    #return redirect(nextUrl)

@login_required
def post_add_interact(request, blog_id=None):
    return post_edit_interact(request, blog_id, None) 
