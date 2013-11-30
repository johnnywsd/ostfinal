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

