from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostCreateForm

def list_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'post': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.profile
            post.save()
            return redirect('users:porfile')
        
    form = PostCreateForm()
    return render(request, 'create_post.html', {'form': form})

def user_posts(request, user):
    post = Post.objects.filter(author__user__username = user)
    return render(request, 'posts.html', {'post': post})




