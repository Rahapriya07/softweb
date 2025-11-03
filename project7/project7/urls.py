from django.contrib import admin
from django.urls import path
from softapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
