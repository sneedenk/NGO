from django.conf.urls import include, url
from donations import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
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
from django.urls import path

app_name = 'donations'
# For use with class based generic views
urlpatterns = [
    #url(r'^(?P<pk>\d+)$', views.ProductDetailsGenericView.as_view(), name='product_details'),
    #url(r'^(?P<pk>\d+)/delete$', views.DeleteProductGenericView.as_view(), name='delete_product'),
    #url(r'^(?P<pk>\d+)/update$', views.UpdateProductGenericView.as_view(), name='update_product'),
    #url(r'^new_product/$', views.NewProductGenericView.as_view(), name='new_product'),
    url(r'^new_user/$', views.CreateUserView.as_view(), name='new_user'),
    #url(r'success$', views.ProductListView.as_view(), name='product_list'),
]
# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# For use with class based views
# urlpatterns = [
#     url(r'^(?P<pk>\d+)$', views.ProductDetailsView.as_view(), name='product_details'),
#     url(r'^(?P<pk>\d+)/delete$', views.DeleteProductView.as_view(), name='delete_product'),
#     url(r'^(?P<pk>\d+)/update$', views.UpdateProductView.as_view(), name='update_product'),
#     url(r'^new_product/$', views.NewProductView.as_view(), name='new_product'),
#     url(r'^new_user/$', views.create_user, name='new_user'),
#     #url(r'success$', views.ProductListView.as_view(), name='product_list'),
# ]

# For use with function based views
# urlpatterns = [
#     url(r'^(?P<pk>\d+)$', views.product_details, name='product_details'),
#     url(r'^(?P<pk>\d+)/delete$', views.delete_product, name='delete_product'),
#     url(r'^new_product/$', views.new_product, name='new_product'),
#     url(r'success$', views.product_list, name='product_list')
# ]
