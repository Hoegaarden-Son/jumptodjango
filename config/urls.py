"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from pybo.views import base_views

from pybo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
    path('a_board/', base_views.index, name='a_board'),
    path('b_board/', base_views.index, name='b_board'),

    # 다른 URL 패턴
    path('privacy/', base_views.privacy, name='privacy'),
    path('terms/', base_views.terms, name='terms'),
]

handler404 = 'common.views.page_not_found'
