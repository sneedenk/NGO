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
from django.conf.urls import include, url
from donations import urls
from donations import views


# For use with class based generic views
urlpatterns = [
    url('admin', admin.site.urls),
    # url(r'^$', views.DonationTypeView.as_view(), name='make_donation'),
    url(r'^donor$', views.DonorInfoView.as_view(), name='donor_info'),
    url(r'^donation$', views.DonationDetailsView.as_view(), name='donor_details'),
    url(r'^event$', views.CreateEventView.as_view(), name='donor_details'),
    url(r'', include(urls, namespace="donations")),
    url(r'accounts/', include(('django.contrib.auth.urls', 'django_accounts'), namespace="django_accounts")),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# possible alternative to ^
# if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# For use with class based views
# urlpatterns = [
#     url('admin', admin.site.urls),
#     url(r'^$', views.ProductListView.as_view(), name='product_list'),
#     url(r'', include(urls, namespace="productapp")),
#     url(r'accounts/', include(('django.contrib.auth.urls', 'django_accounts'), namespace="django_accounts")),
# ]

# For use with function based views
# urlpatterns = [
#     url('admin', admin.site.urls),
#     url(r'^$', views.product_list, name='product_list'),
#     url(r'^', include(urls, namespace="productapp")),
# ]
