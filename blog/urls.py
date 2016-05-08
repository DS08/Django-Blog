"""task URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from .views import(
	blog_create,
	blog_home,
	blog_delete,
	blog_update,
	blog_list,
	blog_detail

	)
urlpatterns = [
	url(r'^$',blog_list,name='list'),
    url(r'^create/$',blog_create),
    url(r'^(?P<id>\d+)/edit/$',blog_update,name="update"),
    url(r'^(?P<id>\d+)/delete/$',blog_delete,name='delete'),
    url(r'^list/$',blog_list),
    url(r'^(?P<id>\d+)/$',blog_detail,name="detail"
),



]
