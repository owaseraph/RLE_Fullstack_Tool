"""
URL configuration for coderun project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.http import FileResponse
import os
from django.conf import settings
from . import views
from history.views import save_history
from history.views import get_history
from history.views import delete_history_item

def serve_react_file(request, filename):
    filepath = os.path.join(settings.BASE_DIR, 'frontend', 'build', filename)
    return FileResponse(open(filepath, 'rb'))
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home_view, name='home'),

    
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='home.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('tool/', views.rle_tool_view, name='rle_tool'),
    path('programming.png', serve_react_file, {'filename': 'programming.png'}),
    path('manifest.json', serve_react_file, {'filename': 'manifest.json'}),
    path('api/save_history/', save_history, name='save_history'),
    path('api/get_history/', get_history, name='get_history'),
    path('api/delete_history/<int:item_id>/', delete_history_item, name='delete_history'),
    path('profile/', views.profile_view, name='profile'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name = 'password_change.html'), name = 'password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name = 'password_change_done.html'), name = 'password_change_done')
    ]
