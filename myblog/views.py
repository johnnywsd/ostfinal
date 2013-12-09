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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from myblog import constant

def home_view(request):
    data_dict = {}
    return render(request, 'home.html', data_dict)

def about_view(request):
    data_dict = {}
    return render(request, 'about.html', data_dict)


def sign_up_view(request):
    data_dict = {}
    return render(request, 'sign_up.html', data_dict)

def login_view(request):
    data_dict = {}
    return render(request, 'login.html', data_dict)

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

def test_page_view(request):
    data_dict = {}
    return render(request, 'long.html', data_dict)

def get_post_list(blogs, current_user_id=None):
    a_list = []
    if(blogs):
        posts = Post.objects.filter(blog__in=blogs).order_by('-create_time')
        for post in posts:
            d = {}
            d['title'] = post.title
            d['id'] = post.id
            content_plain_text = html2text.html2text(post.content)
            d['content'] = content_plain_text[:constant.BRIEF_LENGTH]
            d['author_name'] = post.author.first_name
            d['create_date'] = post.create_time.strftime(settings.DATE_FORMAT)
            d['tags'] = list(post.tags.all())
            if current_user_id and post.author.id==current_user_id:
                d['is_editable'] = True
                
            a_list.append(d)
    return a_list

def latest_post_list_view_bak(request):
    data_dict = {}
    post_list = Post.objects.all().order_by('-create_time')
    #for post in posts:
        #if current_user_id and post.author.id==current_user_id:
            #post.is_editable = True

    paginator = Paginator(post_list, constant.NUM_PER_PAGE )
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    data_dict['posts'] = posts
    return render(request, 'post_list.html', data_dict)

def latest_post_list_view(request):
    data_dict = {}
    post_list = Post.objects.all().order_by('-create_time')
    for post in post_list:
        if post.author.id == request.user.id:
            post.is_editable = True

    data_dict['posts'] = post_list
    data_dict['num_per_page'] = constant.NUM_PER_PAGE
    data_dict['request'] = request #must have
    return render(request, 'post_list.html', data_dict)
