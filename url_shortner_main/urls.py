"""
URL configuration for url_shortner_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import include, path
from url_shortner.views import redirect_url
from .views import homeview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeview, name='home'),
    path('auth/', include('url_users.urls')),
    path('short_url/', include('url_shortner.urls')),
    path('<str:short_key>/', redirect_url, name='redirect_url')
]
