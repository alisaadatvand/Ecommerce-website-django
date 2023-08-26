from django.contrib import admin
from django.urls import include, path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home' ),
    path('accounts/', include('accounts.urls')), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('online/', TemplateView.as_view(template_name='online.html'),name='online'),
    path('teacher/', TemplateView.as_view(template_name='teacher.html'),name='teacher'),
    path('about/', TemplateView.as_view(template_name='about.html'),name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'),name='contact'),

    # admin panel
    # product
    path('panel/', TemplateView.as_view(template_name='./panel/panel.html'),
    name='panel'),
    path('panel/product/',ProductListViewAdmin.as_view(),name='product_view_admin'),
    path('panel/product/new/', ProductCreateView.as_view(), name='product_create'),
    path('panel/product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('panel/product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    #category
    path('panel/category/',CategoryListView.as_view(),name='category_view'),
    path('panel/category/new/', CategoryCreateView.as_view(), name='category_create'),
    path('panel/category/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_update'),
    path('panel/category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    ##city
    path('panel/city/',CityListView.as_view(),name='city_view'),
    path('panel/city/new/', CityCreateView.as_view(), name='city_create'),
    path('panel/city/<int:pk>/', CityDetailView.as_view(), name='city_detail'),
    path('panel/city/<int:pk>/edit/', CityUpdateView.as_view(), name='city_update'), 
    path('panel/city/<int:pk>/delete/', CityDeleteView.as_view(), name='city_delete'),

    ##Teacher
    path('panel/Teacher/',TeacherListView.as_view(),name='Teacher_view'),
    path('panel/Teacher/new/', TeacherCreateView.as_view(), name='Teacher_create'),
    path('panel/Teacher/<int:pk>/', TeacherDetailView.as_view(), name='Teacher_detail'),
    path('panel/Teacher/<int:pk>/edit/', TeacherUpdateView.as_view(), name='Teacher_update'), 
    path('panel/Teacher/<int:pk>/delete/', TeacherDeleteView.as_view(), name='Teacher_delete'),

    #stock
    path('panel/stock/',StockListView.as_view(),name='stock_view'),
    path('panel/stock/new/', StockCreateView.as_view(), name='stock_create'),
    path('panel/stock/<int:pk>/', StockDetailView.as_view(), name='stock_detail'),
    path('panel/stock/<int:pk>/edit/', StockUpdateView.as_view(), name='stock_update'), 
    path('panel/stock/<int:pk>/delete/', StockDeleteView.as_view(), name='stock_delete'),
    

    path('ComingSoon/', TemplateView.as_view(template_name='ComingSoon.html'),name='ComingSoon'),
    path('Album/', TemplateView.as_view(template_name='album.html'),name='album'),
    path('store/', include('store.urls')),
     path('', include('accounts.urls')),
    path('cart/', include('carts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
