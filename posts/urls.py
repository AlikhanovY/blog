from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.list_posts, name='list_posts'),
    path('create', views.create_post, name='create_post'),
    path('edit/<int:post_id>', views.edit_post, name='edit_post'),
    path('<str:user>', views.user_posts, name='user_posts'),
    path('comment/all', views.list_comments, name='list_comments'),
    path('comment/<int:post_id>', views.create_comment, name='create_comment'),
    path('comment/edit/<int:comment_id>', views.edit_comment, name='edit_comment'),

]