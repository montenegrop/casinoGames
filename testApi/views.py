from rest_framework import generics
from testModel.models import JugadaTest

from .serializers import JugadaSerializer

# from .serializer import PostSerializer


class JugadaList(generics.ListCreateAPIView):
    queryset = JugadaTest.objects.all()
    serializer_class = JugadaSerializer


class JugadaDetail(generics.RetrieveDestroyAPIView):
    queryset = JugadaTest.objects.all()
    serializer_class = JugadaSerializer

    # lookup_field = 'numero'
