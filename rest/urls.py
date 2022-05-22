
from django.urls import path
from .views import dummy_casino_json

app_name = 'jsons de prueba'

# urlpatterns = [
#     path('<int:pk>/', JugadaDetail.as_view(), name='rollcreate'),
#     path('', JugadaList.as_view(), name='allrolls'),
#     # path('numero/<int:numero>/', PostDetail.as_view(), name='detailcreateNumero'),
# ]

urlpatterns = [
    path('dama_muerta/', dummy_casino_json, name='dama_muerta'),
]