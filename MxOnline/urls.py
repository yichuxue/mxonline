"""MxOnline URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.urls import re_path, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.static import serve
import xadmin
from MxOnline.settings import MEDIA_ROOT
from users.urls import IndexView


urlpatterns = [
    re_path('^xadmin/', xadmin.site.urls),
    re_path('^$', IndexView.as_view(), name='index'),
    re_path('', include('users.urls')),
    re_path('^captcha/', include('captcha.urls')),

    re_path('^org/', include('organization.urls')),

    re_path('^course/', include('courses.urls')),

    # 配置上传文件的访问处理函数
    re_path('^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),




    # re_path('^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),

]


# 全局404页面
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'
