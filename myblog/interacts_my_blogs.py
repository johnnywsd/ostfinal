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
from myblog import constant
from myblog import utils


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
            tags_str = form.cleaned_data['tags'].strip()
            tag_names = tags_str.split(',')
            tags = []
            if not tags_str:
                tag_names = [constant.NO_TAG]

            for tag_name in tag_names:
               tag, res = Tag.objects.get_or_create(name=tag_name,
                       defaults={'name': tag_name}) 
               tags.append(tag)

            if post_id:
                post = Post.objects.get(pk=post_id)
            else:
                post = Post()

            blog_id = form.cleaned_data['blog_id']
            if blog_id:
                post.blog = Blog.objects.get(pk=blog_id)
            post.title = title
            post.content = utils.plain2link(content)
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

@login_required
def post_delete_interact(request, post_id):
    user = request.user
    post = Post.objects.get(pk=post_id)
    blog = post.blog
    blog_id = blog.id
    if user.id == blog.creator.id:
        nextUrl = reverse('my_blogs_own_view', kwargs={'blog_id': blog_id})
    elif user in blog.authors :
        nextUrl = reverse('my_blogs_shared_view', kwargs={'blog_id': blog_id})
    post.delete()
    return HttpResponseRedirect(nextUrl)
    
@login_required
def blog_edit_interact(request):
    user = request.user
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog_id = form.cleaned_data['blog_id']
            blog_name = form.cleaned_data['name']
            author_ids_str = form.cleaned_data['author_emails'].strip()
            if author_ids_str:
                author_ids = author_ids_str.split(',')
                try:
                    author_ids.remove(str(user.id))
                except:
                    pass
                #return HttpResponse(author_ids)
                authors = User.objects.filter(pk__in=author_ids)
            else:
                authors = []
            
            if not blog_id: #create new blog
                blog = Blog()
            else:
                blog = Blog.objects.get(pk=blog_id)

            blog.name = blog_name
            blog.creator = user
            blog.save()
            blog.authors =authors
            blog.save()
    nextUrl = reverse('my_blogs_view')
    return HttpResponseRedirect(nextUrl)

@login_required
def blog_delete_interact(request, blog_id):
    user = request.user
    blog = Blog.objects.get(pk=blog_id)
    if user.id == blog.creator.id:
        blog.delete()
    nextUrl = reverse('my_blogs_view')
    return HttpResponseRedirect(nextUrl)

@login_required
def blog_revoke_interact(request, blog_id):
    user = request.user
    blog = Blog.objects.get(pk=blog_id)
    #return HttpResponse(blog.authors.all())
    #if user.id in [x.id for author in blog.authors.all()] :
    if user in blog.authors.all():
        blog.authors.remove(user)
        blog.save()
    nextUrl = reverse('my_blogs_view')
    return HttpResponseRedirect(nextUrl)
