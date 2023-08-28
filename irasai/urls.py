from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='homepage-url'),
    path('artistai/', views.artistai, name='artistai-visi-url'),
    path('artistai/<int:artistas_id>', views.artistas, name='artistas-vienas-url'),

]