"""DjangoEcommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from DjangoEcommerceApp import views as appViews

from . import settings, adminViews
from django.conf.urls.static import static

urlpatterns = [
    path('administrator/', admin.site.urls),
    path('admin/', appViews.adminLogin,name="Admin Login"),
    path('demo/',appViews.demoPage,name="Demo Page"),
    path('demoPage/',appViews.demoPageTemplate,name="Demo Page template"),
    # Categories
    path('category_list/',adminViews.CategoriesListView.as_view(),name='category_list_view'),
    path('category_create/',adminViews.CategoriesCreateView.as_view(),name='category_create_view'),
    path('category_update/<slug:pk>/',adminViews.CategoriesUpdateView.as_view(),name='category_update_view'),
    # Subcategories
    path('sub_category_list/',adminViews.SubCategoriesListView.as_view(),name='sub_category_list_view'),
    path('sub_category_create/',adminViews.SubCategoriesCreateView.as_view(),name='sub_category_create_view'),
    path('sub_category_update/<slug:pk>/',adminViews.SubCategoriesUpdateView.as_view(),name='sub_category_update_view'),
    # Merchant User
    path('merchant_create/',adminViews.MerchantUserCreateView.as_view(),name="merchant_create_view"),
    path('merchant_list/',adminViews.MerchantUserListView.as_view(),name="merchant_list_view"),
    path('merchant_update/<slug:pk>',adminViews.MerchantUserUpdateView.as_view(),name="merchant_update_view"),
    # Page for admin
    path('admin-home/',adminViews.admin_home,name="adminHome"),
    path('admin-login/',appViews.adminLoginProcess,name="admin-login-process"),
    path('admin-logout/',appViews.adminLogoutProcess,name="admin-logout-process"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_name=settings.STATIC_ROOT)
# This addition of the static files make the django application
# to get the static files with page and makes the static files
# accesible to site.
