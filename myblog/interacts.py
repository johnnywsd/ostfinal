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


def sign_up_interact(request):
    email = request.POST.get('email')
    username = email 
    password = request.POST.get('password')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    
    if not username:
        return HttpResponse("Email is required")
    
    tmp = User.objects.filter(username = username)
    if len(tmp) < 1:
        user = User()
        user.set_password(password)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        user = authenticate(username=username, password=password)
        login(request,user)
        nextUrl = reverse('home')
        return HttpResponseRedirect(nextUrl)
    else:
        return HttpResponse("Please choose another username, this one is occupied!")


def login_user(request):
    username = password = ''
    nextUrl = nextUrlDefault = reverse('home')

    if request.POST:
        username = request.POST.get('username')
        email = request.POST.get('email')
        if not username and email:
            username = email

        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        nextUrl = request.POST.get('next')
        if not nextUrl or nextUrl=='':
            nextUrl = nextUrlDefault
        
        if user is not None:
            if user.is_active:
                login(request, user)
                #user_profile = UserProfile.objects.filter(user = user)
                #if not user_profile:
                    #user_profile = UserProfile()
                    #user_profile.user = user
                    ##user_profile.name = user.username
                    #user_profile.save()
                return HttpResponseRedirect(nextUrl)
        else:
            return HttpResponse("Account Password Incrrect!")

@login_required
def logout_user(request):
    logout(request)
    return redirect(settings.LOGIN_URL)

