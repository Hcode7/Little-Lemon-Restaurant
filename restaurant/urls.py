from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('menu/', views.menu_view, name='menu'),
    path('menu/detail/<slug:slug>/<int:id>/', views.menu_detail, name='menu_detail'),
    path('reserve/', views.booking_vieW, name='reserve'),
    path('booking/', views.booking, name='book'),
    path('update/<int:pk>/', views.update_booking, name='update')
]