from django.contrib import admin
from django.urls import path
from fail_App import views

urlpatterns = [
    path('', views.index, name='home'),
    path('follow/', views.follow, name='follow'),
    path('media/', views.media, name='media'),
    path('profile/', views.profile, name='profile'),
    path('request/', views.requests, name='request'),
    path('setting/', views.setting, name='setting'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('signup/', views.Signup, name='signup'),
]
