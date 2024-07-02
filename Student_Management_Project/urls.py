"""
URL configuration for Student_Management_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from . import STAFF_views,STUDENT_views,HOD_views,views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base,name="base_view"),
    path('', views.login,name="login"),
    path('Dologin', views.Do_login,name="Dologin"),
    path('HOD/home', HOD_views.home,name="HOD_home"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
