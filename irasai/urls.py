from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='homepage-url'),
    path('artistai/', views.artistai, name='artistai-visi-url'),
    path('artistai/<int:artistas_id>', views.artistas, name='artistas-vienas-url'),
    path('irasai/', views.IrasasListView.as_view(), name='irasai-visi-url'),
    path('irasai/<int:pk>', views.IrasasDetailView.as_view(), name='irasas-vienas-url'),
    path('paieska/', views.search, name='paieska-url'),
]