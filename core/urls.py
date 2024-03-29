"""
URL configuration for core project.

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

from mainAPP.views import *

urlpatterns = [

                  path('admin/', admin.site.urls),
                  path('', Home.as_view(), name='home'),
                  path('about/', About.as_view(), name='about'),
                  path('blog/', Blog.as_view(), name='blog'),
                  path('<str:pk>/maqola/', Maqola.as_view(), name='maqola'),
                  path('<int:pk>/delete/', Delete.as_view(), name='delete'),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
