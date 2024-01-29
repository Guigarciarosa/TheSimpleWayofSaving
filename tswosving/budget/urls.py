# budget/urls.py

from django.urls import path
from .views import cadastrar_usuario

urlpatterns = [
    path('cadastrar-usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    # Adicione mais URLs conforme necessário
]
