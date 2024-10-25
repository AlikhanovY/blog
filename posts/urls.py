from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.list_posts, name='list_posts'),
    path('create', views.create_post, name='create_post'),
    path('<str:user>', views.user_posts, name='user_posts'),



]