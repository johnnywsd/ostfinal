from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.conf import settings
from django.http import Http404
from myblog.models import Blog
from myblog.models import Post
from myblog.models import Tag
from django.db.models import Q

import json


@login_required
def my_blogs_view(request):
    data_dict = {}
    user = request.user
    #own_blogs = Blog.objects.filter(creator=user)

    #author_blogs = user.blog_set.all()
    #return HttpResponse('<br>'.join(dir(own_blogs[0].authors)))
    #user = User.objects.get(pk = user.id)
    #return HttpResponse('<br>'.join(dir(user)))
    own_blogs = user.creator_blogs.all()
    author_blogs = user.author_blogs.filter(~Q(creator=user))
    follower_blogs = user.follower_blogs.all()

    data_dict['own_blogs'] = own_blogs
    data_dict['author_blogs'] = author_blogs 
    data_dict['follower_blogs'] = follower_blogs
    return render(request, 'my_blogs.html', data_dict)

def get_post_list_by_id(blog_ids):
    a_list = []
    if(blog_ids):
        posts = Post.objects.filter(blog__id__in=blog_ids).order_by('-create_time')
    for post in posts:
        d = {}
        d['title'] = post.title
        d['content'] = post.content[:500]
        d['author_name'] = post.author.first_name
        d['create_date'] = post.create_time.strftime(settings.DATE_FORMAT)
        a_list.append(d)
    return a_list

def get_post_list(blogs):
    a_list = []
    if(blogs):
        posts = Post.objects.filter(blog__in=blogs).order_by('-create_time')
    for post in posts:
        d = {}
        d['title'] = post.title
        d['id'] = post.id
        d['content'] = post.content[:500]
        d['author_name'] = post.author.first_name
        d['create_date'] = post.create_time.strftime(settings.DATE_FORMAT)
        d['tags'] = list(post.tags.all())
        a_list.append(d)
    return a_list

@login_required
def my_blogs_own_view(request, blog_id=None):
    data_dict ={}
    user = request.user
    a_list = []
    author_names_set = set()

    if(blog_id):
        blog = Blog.objects.get(pk=blog_id)
        blogs = [blog,]
        data_dict['info_title'] = blog.name
        data_dict['owner'] = blog.creator.first_name
        data_dict['blog_id'] = blog_id
        
    else:
        blogs = user.creator_blogs.all();
        data_dict['info_title'] = 'Blogs I Own'
        data_dict['blog_id'] = 0

    a_list = get_post_list(blogs)

    for blog in blogs:
        authors = blog.authors.all()
        for author in authors:
            author_names_set.add(author.first_name)

    data_dict['author_names'] = ', '.join(author_names_set)
    data_dict['post_num'] = len(a_list)
    data_dict['posts'] = a_list
    data_dict['is_editable'] = True
    return render(request, 'post_list_own.html', data_dict)

@login_required
def my_blogs_shared_view(request, blog_id=None):
    data_dict ={}
    user = request.user
    author_names_set = set()

    if(blog_id):
        blog = Blog.objects.get(pk=blog_id)
        blogs = [blog,]
        data_dict['info_title'] = blog.name
        data_dict['owner'] = blog.creator.first_name
        
    else:
        blogs = user.author_blogs.filter(~Q(creator=user));
        data_dict['info_title'] = 'Blogs Shared with Me'

    a_list = get_post_list(blogs)

    for blog in blogs:
        authors = blog.authors.all()
        for author in authors:
            author_names_set.add(author.first_name)

    data_dict['author_names'] = ', '.join(author_names_set)
    data_dict['post_num'] = len(a_list)
    data_dict['posts'] = a_list
    return render(request, 'post_list_shared.html', data_dict)

@login_required
def my_blogs_following_view(request, blog_id=None):
    data_dict ={}
    user = request.user
    author_names_set = set()

    if(blog_id):
        blog = Blog.objects.get(pk=blog_id)
        blogs = [blog,]
        data_dict['info_title'] = blog.name
        data_dict['owner'] = blog.creator.first_name
        
    else:
        blogs = user.follower_blogs.all();
        data_dict['info_title'] = 'Blogs I Following'

    a_list = get_post_list(blogs)

    for blog in blogs:
        authors = blog.authors.all()
        for author in authors:
            author_names_set.add(author.first_name)

    data_dict['author_names'] = ', '.join(author_names_set)
    data_dict['post_num'] = len(a_list)
    data_dict['posts'] = a_list
    return render(request, 'post_list_following.html', data_dict)

@login_required
def post_detail_embedded_view(request, post_id=None):
    data_dict = {}
    a_list = []
    if(post_id):
        post = Post.objects.get(pk=post_id)
        data_dict['post'] = post
        data_dict['create_date'] = post.create_time.strftime(settings.DATE_FORMAT)
        data_dict['author_name'] = post.author.first_name
        data_dict['content'] = post.content
        #data_dict['post_id'] = post_id
        if post.author.id == request.user.id:
            data_dict['is_editable'] = True
    return render(request, 'post_embedded.html', data_dict)

@login_required
def post_edit_embedded_view(request, blog_id=None, post_id=None):
    data_dict = {}
    user = request.user
    if(post_id):
        post = Post.objects.get(pk=post_id)
        data_dict['post'] = post
        blog_id = post.blog.id
        #data_dict['post_id'] = post_id
        data_dict['create_date'] = post.create_time.strftime(settings.DATE_FORMAT)
        data_dict['author_name'] = post.author.first_name
        data_dict['content'] = post.content
        tags = post.tags.all()
        tags_dict = {}
        tags_list = []
        for tag in tags:
            #tags_dict[tag.id] = tag.name
            tags_list.append(tag.name)
        #data_dict['tags_json'] = json.dumps(tags_dict)
        data_dict['tags_json'] = json.dumps(tags_list)

    blog_options = user.author_blogs.all()

    
    data_dict['blog_options'] = blog_options
    data_dict['blog_id'] = blog_id
    all_tags = Tag.objects.all().order_by('name')
    all_tags_list = [x.name for x in all_tags]
    all_tags_json = json.dumps(all_tags_list)
    data_dict['all_tags_json'] = all_tags_json

            
    return render(request, 'post_embedded_edit.html', data_dict)

