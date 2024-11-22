from django.contrib import admin
from django.urls import path
from vacateapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('starter/', views.starter),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('service/', views.services, name='service'),
    path('book/', views.books, name='book'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('', views.register, name='register'),

]
