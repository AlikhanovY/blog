from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path('', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('profile/<str:user>/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),



]