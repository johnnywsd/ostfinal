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
from django.db.models import Q


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
        d['content'] = post.content[:500]
        d['author_name'] = post.author.first_name
        d['create_date'] = post.create_time.strftime(settings.DATE_FORMAT)
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
        
    else:
        blogs = user.creator_blogs.all();
        data_dict['info_title'] = 'Blogs I Own'

    a_list = get_post_list(blogs)

    for blog in blogs:
        authors = blog.authors.all()
        for author in authors:
            author_names_set.add(author.first_name)

    data_dict['author_names'] = ', '.join(author_names_set)
    data_dict['post_num'] = len(a_list)
    data_dict['posts'] = a_list
    return render(request, 'post_list_own.html', data_dict)

@login_required
def my_blogs_shared_view(request, blog_id=None):
    data_dict ={}
    user = request.user
    a_list = []
    author_names_set = set()

    if(blog_id):
        blog = Blog.objects.get(pk=blog_id)
        blogs = [blog,]
        data_dict['info_title'] = blog.name
        
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
    return render(request, 'post_list_own.html', data_dict)

@login_required
def my_blogs_following_view(request):
    pass
