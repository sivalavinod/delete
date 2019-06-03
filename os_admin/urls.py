"""online URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from os_admin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_home/',TemplateView.as_view(template_name='admin/admin_login.html')),
    path('adminwel/',TemplateView.as_view(template_name='admin/admin_welcome.html')),
    path('adminwelcome1/',TemplateView.as_view(template_name='admin/welcome_admin.html')),
    path('agentdatasave/',views.agentdatasave),
    path('agent_delete/',views.agent_delete),
    path('admin_login/',views.admin_login),
    path('afteotp/',views.otpvalidation),
    path('agentwelcome1/',views.agentelcome),
    path('agent_logout/',views.logoutadmin)
]
