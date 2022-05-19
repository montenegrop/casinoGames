from django.urls import path
from .views import JugadaList, JugadaDetail

app_name = 'test_api'

urlpatterns = [
    path('<int:pk>/', JugadaDetail.as_view(), name='rollcreate'),
    path('', JugadaList.as_view(), name='allrolls'),

    # path('numero/<int:numero>/', PostDetail.as_view(), name='detailcreateNumero'),

]