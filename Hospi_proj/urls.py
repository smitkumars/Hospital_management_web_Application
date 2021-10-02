"""Hospi_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
#from Django_project.Hospi_proj.clinic_app.views import ContactDetailView, create, edit


from django import template
#from django.contrib import admin
from django.urls import path, include
from clinic_app import views
from django.conf.urls import include
from django.views.generic.base import TemplateView # new
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('patient/',views.IndexView.as_view(),name='index'),
    path('patient/<int:pk>/',views.ContactDetailView.as_view(),name='detail'),
    path('patient/edit/<int:pk>/',views.edit,name='edit'),
    path('patient/create/',views.create,name='create'),
    path('patient/delete/<int:pk>/',views.delete,name='delete'),

   # path('', TemplateView.as_view(template_name='clinic_app/index.html'), name='home'),

    ##### user related path##########################
    path('',include('accounts.urls')),
    

    
]
