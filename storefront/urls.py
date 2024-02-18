"""
URL configuration for storefront project.

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
from django.urls import path, include
import debug_toolbar
from . import views

urlpatterns = [
    path('', views.show_home_page, name='index'),
    path('admin/', admin.site.urls),
    path('about/', views.show_about_page),
    path('todo/', include('todo.urls')), # if the path start with todo, django will let the app todo.urls handle the requests
    path('__debug__/', include('debug_toolbar.urls')),
]
