from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path('', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('profile/<str:user>/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('follow/<int:user_id>', views.follow_user, name='follow'),
    path('unfollow/<int:user_id>', views.unfollow_user, name='unfollow')
]