from django.urls import path, include
from . import views

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register_view, name='register')
]