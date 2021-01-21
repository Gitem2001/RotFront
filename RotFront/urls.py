"""RotFront URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views
from apps.core.views import frontpage, signup
from apps.feed.views import feed, search
from apps.feed.api import api_add_rot
from apps.RotFrontprofile.views import RotFrontprofile, edit_profile, follow_roter, unfollow_roter, followers, follows
urlpatterns = [
    #
    #

    path('', frontpage, name='frontpage'),
    path('signup/',signup,name='signup'),
    path('logout/',views.LogoutView.as_view(), name='logout'),
    path('login/',views.LoginView.as_view(template_name='core/login.html'),name='login'),
    #
    path('feed/',feed,name='feed'),
    path('search/',search,name='search'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('u/<str:username>/', RotFrontprofile, name='RotFrontprofile'),
    path('u/<str:username>/followers/', followers, name='followers'),
    path('u/<str:username>/follows/', follows, name='follows'),
    path('u/<str:username>/follow/', follow_roter, name='follow_roter'),
    path('u/<str:username>/unfollow/', unfollow_roter, name='unfollow_roter'),
    #
    #API
    path('api/add_rot/',api_add_rot,name='api_add_rot'),
    #Admin
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
