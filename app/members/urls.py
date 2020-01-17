from django.urls import path, include

from . import views

app_name = 'members'
urlpatterns = [
    path('signup/', views.signup_view, name='signup'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('naver-login/', views.naver_login, name='naver-login'),


]
