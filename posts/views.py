from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Post, Comment
from .forms import PostCreateForm, CommentCreateForm

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
            profile_url = reverse('users:profile', args=[request.user.username])
            return redirect(profile_url)
        
    form = PostCreateForm()
    return render(request, 'create_post.html', {'form': form})

def edit_post(request, post_id):
    post = Post.objects.filter(id=post_id)
    if request.method == "POST":
        form = PostCreateForm(request.post)
        if form.is_valid():
            form.save()
    form = PostCreateForm()
    return render(request, 'create_post', {'form': form})

def user_posts(request, user):
    post = Post.objects.filter(author__user__username = user)
    return render(request, 'posts.html', {'post': post})

def create_comment(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    if request.method == "POST":
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user.profile
            comment.save()
    form = CommentCreateForm()
    return render(request, 'create_comment.html', {'form': form})

def edit_comment(request, comment_id):
    comment = Comment.objects.filter(id = comment_id)
    if request.method == "POST":
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            form.save()
    form = CommentCreateForm()
    return render(request, 'create_comment.html', {'form': form})

def list_comments(request):
    comment = Comment.objects.all()
    return render(request, 'comments.html', {'comment':comment})






