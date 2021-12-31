from django.shortcuts import render
from user.forms import RegistrationForm, LoginForm, PostForm
from user.models import User
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == "POST":
        regform = RegistrationForm(request.POST)
        if regform.is_valid():
            regform.save()
            loginform = LoginForm()
            return render(request, 'user/login.html', {'loginform':loginform})
        else:
            regform = RegistrationForm()
            return render(request, 'user/reg.html', {'regform': regform})
    else:
        regform = RegistrationForm()
        return render(request, 'user/reg.html', {"regform": regform})

def login(request):
    if request.method == "POST":
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            un = loginform.cleaned_data['username']
            pw = loginform.cleaned_data['password']
            dbuser = User.objects.filter(username=un, password=pw)
            if not dbuser:
                return render(request, 'user/reg.html')
            else:
                postform = PostForm()
                return render(request, 'post.html', {'postform': postform})
    else:
        loginform = LoginForm()
        return render(request, 'user/login.html', {'loginform':loginform})


def Post(request):
    if request.method == "POST":
        postform = PostForm(request.POST)
        if postform.is_valid():
            postform.save()
            return HttpResponse("posted successfully")
    else:
        postform = PostForm()
        return render(request, 'post.html', {'postform': postform})


