from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('', views.post_list, name='post_list'),
    path("register/", views.register, name="register"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/change_password/', views.change_password, name='change_password'),
    path('post/<int:pk>/comment/new/', views.comment_new, name='comment_new'),
    path('post/<int:post_pk>/comment/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
]