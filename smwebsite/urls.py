"""smwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('', views.home, name='home'),
    #URLs for UCArpooling
    path('UCArpooling/', views.ucarpooling, name='ucarpooling'),
    path('UCArpooling/experimento', views.ucarpoolingExperiment, name='ucarpoolingExperiment'),
    path('UCArpooling/guia-voluntario', views.ucarpoolingGuide, name='ucarpoolingGuide'),
    #URLs for SmartParking
    path('SmartParking/', views.smartparking, name='smartparking'),
    #URLs for SmartMoving
    path('SmartMoving/', views.smartmoving, name='smartmoving'),
    #URL for the blog site, news from the project
    path('blog/', views.blog, name='blog'),
    #URL for the dissemination results site, articles, presentations from the project
    path('dissemination/', views.dissemination, name='dissemination'),
)

# urlpatterns += [
#     path('', views.home, name='home'),
# ]
