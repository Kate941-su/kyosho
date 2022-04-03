#アプリケーション側ルーティング設定

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import forms, views
from datetime import datetime

app_name = "app"

urlpatterns = [
    path('', views.home, name = 'home'),
    path('home/', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('logout/', LogoutView.as_view(next_page = '/'), name = 'logout'),
    path('upload/', views.modelFormUpload, name = 'upload'),
    path('dotArt/', views.viewFilter, name = 'dotArt'),
    path('mosaic/', views.viewFilter, name = 'mosaic'),
    path('subColor/', views.viewFilter, name = 'subColor'),
    path('threshold/', views.viewFilter, name = 'threshold'),
    path('gauss/', views.viewFilter, name = 'gauss'),
    path('edge/', views.viewFilter, name = 'edge'),
    path('medianFilter/', views.viewFilter, name = 'medianFilter'),
    path('WBComic/', views.viewFilter, name = 'WBComic'),
    path('pencil/', views.viewFilter, name = 'pencil'),
    path('AIAnimeArt', views.viewFilter, name = 'AIAnimeArt'),
    path('creatingColoringBook/', views.viewFilter, name = 'creatingColoringBook'),
    path('stylization/', views.viewFilter, name = 'stylization'),
    path('grayScale/', views.viewFilter, name = 'grayScale'),
#    path('edit/<int:num>', views.edit, name='edit'),
    path('login/',
        LoginView.as_view
        (
            template_name='app/login.html',
            authentication_form=forms.BootstrapAuthenticationForm,
            extra_context=
            {
                'title': 'Log in',
                'year' : datetime.now().year,
            }
        ),
        name='login'), 
]

