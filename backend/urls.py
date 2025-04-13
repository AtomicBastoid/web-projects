"""
URL configuration for backend project.

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
import  django.contrib.auth.urls as auth_urls
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views as backend_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("qrcode", include('QRCode.urls')),
    path('', backend_views.index, name='index'),
    path('contact/', backend_views.contact, name='contact'),
    path('yt_downloader/', include('yt_downloader.urls')),
    path('', include(auth_urls), name='auth'),
    path('', include('registration.urls'), name='user_handling'),
    path('', include('blog.urls'), name='postsApp')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)