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
from django.db.models import Q

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
