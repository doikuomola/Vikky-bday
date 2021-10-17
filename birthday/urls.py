
from django.urls import path

from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('live/', views.live, name='live'),
    path('createwish', views.createwish, name='createwish'),
    path('wishes', views.wishes, name='wishes'),
]
