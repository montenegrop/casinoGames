
from django.urls import path
from .views import dummy_casino_json, dummy_victorious_json, realistic_victorious_json, victorious

app_name = 'jsons de prueba'

# urlpatterns = [
#     path('<int:pk>/', JugadaDetail.as_view(), name='rollcreate'),
#     path('', JugadaList.as_view(), name='allrolls'),
#     # path('numero/<int:numero>/', PostDetail.as_view(), name='detailcreateNumero'),
# ]

urlpatterns = [
    path('dama_muerta/', dummy_casino_json, name='dama_muerta'),
    path('victorious_style/', dummy_victorious_json, name='victorious_style'),
    path('realistic_victorious/', realistic_victorious_json,
         name='realistic_victorious'),
    path('victorious/', victorious,
         name='victorious')
]
