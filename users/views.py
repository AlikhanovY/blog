from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileLoginForm, ProfileRegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from posts.models import Post



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




