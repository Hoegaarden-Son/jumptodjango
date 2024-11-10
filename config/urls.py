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
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from pybo.views import base_views

# 기본 언어 설정이 없는 URL 패턴 (예: /admin)
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
    path('pybo/', include('pybo.urls')),
]

# 언어별 URL 패턴을 포함한 i18n_patterns
urlpatterns += i18n_patterns(
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),

    path('a_board/', base_views.index, name='a_board'),
    path('b_board/', base_views.index, name='b_board'),

    path('common/', include('common.urls')),
    path('privacy/', base_views.privacy, name='privacy'),
    path('terms/', base_views.terms, name='terms'),
)

handler404 = 'common.views.page_not_found'
