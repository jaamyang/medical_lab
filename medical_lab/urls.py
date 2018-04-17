"""medical_lab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from homesite.admin import admin_site
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myadmin/', admin_site.urls),
    path('',views.home,name = 'home'),
    path('activities/',views.activities,name = 'activity'),
    path('intro/',views.intro,name = 'intro'),
    path('members/',views.members,name = 'members'),
    path('achievements/',views.achievements,name = 'achievements'),
    path('login/',views.login,name = 'login'),
    path('detail/<int:text_pk>',views.text_detail,name = 'text_detail'),
    path('ckeditor',include('ckeditor_uploader.urls')),
    path('download/',include('download.urls')),
    path('logout/',views.logout_view,name = 'logout'),

]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
