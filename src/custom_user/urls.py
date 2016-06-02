"""customauth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import login, loggedin, auth_view, logout, invalid_login, register_user, register_success

urlpatterns = [
	url(r'^login/$', login),
	url(r'^auth/$', auth_view),
	url(r'^logout/$', logout),
	url(r'^loggedin/$', loggedin),
	url(r'^invalid/$', invalid_login),
	url(r'^register/$', register_user),
	url(r'^register_success/$', register_success),
]