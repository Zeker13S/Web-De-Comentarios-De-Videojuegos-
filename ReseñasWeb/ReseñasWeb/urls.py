"""
URL configuration for ReseñasWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [

    # Inicio
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    # Links Internos

    path('newworld/',views.newworld, name='newworld'),
    path('finalfantasy/',views.finalfantasy, name='finalfantasy'),
    path('lostark/',views.lostark, name='lostark'),
    path('wow/',views.wow, name='wow'),
    path('albion/',views.albion, name='albion'),
    
    path('post/<post_title>', views.view_post, name='view_post'),
    path('post/<post_title>/like', views.like_post, name='like_post'),
    path('post/<str:post_title>/comment',  views.add_comment, name='add_comment'),
    path('profile/<str:user>', views.view_profile, name='profile'),
    path('delete_user/<user>', views.delete_user, name='delete_user'),
    path('post_created/', views.post_created, name='post_created'),
    path('delete/<post_title>', views.delete_post, name='delete_post'),
    
    # Registro

    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
]
