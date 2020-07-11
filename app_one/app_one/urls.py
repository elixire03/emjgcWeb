"""app_one URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from main_app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^message_validator/', include('main_app.urls')),
    url(r'^sliders/', views.sliders, name = "slider"),
    url(r'^aboutus/', views.aboutus, name = "service"),
    url(r'^services/', views.services, name = "service"),
    url(r'^add_slider/', views.add_slider, name = "add_slider"),
    url(r'^edit_slider/', views.edit_slider, name = "edit_slider"),
    url(r'^list_slider/', views.list_slider, name = "list_slider"),   
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static (settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


