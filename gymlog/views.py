from django.shortcuts import render
from django.shortcuts import render,HttpResponse, HttpResponseRedirect, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from gymlog.models import Comment, Profile, Gym, Post

# Create your views here.
def navbar_view(request):
    return render(request, 'navbar.html')

@login_required
def index(request):
    template_name = 'index.html'
    posts = Post.objects.all()
    return render(request, template_name, {"posts": posts})
