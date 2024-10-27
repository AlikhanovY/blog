from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileLoginForm, ProfileRegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from posts.models import Post
from .models import Follow



def login_user(request):
    if request.method == 'POST':
        form = ProfileLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            authentication = authenticate(request, username=username, password=password)
            if authentication is not None:
                login(request, authentication)
                return redirect(f'profile/{authentication.username}')
        else:
            print(form.errors)  
            messages.error(request, 'Invalid login credentials.')
    else:
        form = ProfileLoginForm()
        
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = ProfileRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration success')
            return redirect('login')
    else:
        form = ProfileRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request, user):
    profile_user = get_object_or_404(User, username=user)
    posts = Post.objects.filter(author__user__username = user)
    return render(request, 'profile.html', {'user': profile_user, 'posts': posts})

def logout_view(request):
    logout(request)
    return redirect('users:login')


@login_required
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    print(user_to_follow.username)
    if not request.user.following.filter(id=user_id):
        print(request.user.username)
        Follow.objects.create(follower=request.user, following=user_to_follow)
    return render(request, 'profile.html')


@login_required
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    request.user.following.filter(id=user_id).delete()
    return render(request, 'profile.html')






