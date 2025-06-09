from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('listaCanetas/', views.listaCanetas, name='listaCanetas'),
    path('novaCaneta', views.novaCaneta, name='novaCaneta'),
    path('editar/<int:caneta_id>/', views.editarCaneta, name='editarCaneta'),
    path('excluir/<int:caneta_id>/', views.excluirCaneta, name='excluirCaneta')
]

