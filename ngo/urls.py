"""inventory_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls import url
from donations import urls
from donations import views
from django.urls import path, include

# For use with class based generic views
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.EventListView.as_view(), name='list_events'),
    url(r'^event$', views.CreateEventView.as_view(), name='create_event'),
    url(r'', include(urls, namespace="donations")),
    path('usr/', include('users.urls')),

    #url(r'accounts/', include(('django.contrib.auth.urls', 'django_accounts'), namespace="django_accounts")),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
