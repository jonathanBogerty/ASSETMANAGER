from django.shortcuts import render
from datetime import datetime
from . import forms
from django.contrib.auth import login, authenticate

def index(request):
    now = datetime.now()

    return render(
        request,
        "Application/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'title' : "Hello Django",
            'message' : "Hello Django!",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )

def about(request):
   return render(
      request,
      "Application/about.html",
      {
         'title' : "About",
         'content' : "This is an asset manager."
      }
   )

def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
            else:
                message = 'Login failed!'
    return render(
        request, 'application/login.html', context={'form': form, 'message': message})