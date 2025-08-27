from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('foto/<int:id>/', views.foto_detail, name='foto_detail'),
    path('pesquisar/', views.pesquisar_fotos, name='pesquisar_fotos'),
]