"""baemin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from partner import views

urlpatterns = [
    #url(r'^partner/', include('partner.urls')),
    url(r'^admin/', admin.site.urls),
    #url(r'^$', views.index, name='index'),
    url(r'^partner/$', views.index, name='index'),
    url(r'^partner/signup/$', views.signup, name='signup'),
    url(r'^partner/login/$', views.login, name='login'),
    url(r'^partner/logout/$', views.logout, name='logout'),
    url(r'^partner/edit/$', views.edit_info, name='edit'),
    url(r'^partner/menu/$', views.menu, name='menu'),
    url(r'^partner/menu/add/$', views.menu_add, name='menu_add'),
    url(r'^partner/menu/(?P<menu_id>\d+)/$', views.menu_detail, name='menu_detail'),
    url(r'^partner/menu/(?P<menu_id>\d+)/edit/$', views.menu_edit, name='menu_edit'),
    url(r'^partner/menu/(?P<menu_id>\d+)/delete/$', views.menu_delete, name='menu_delete'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
