from rest_framework import serializers
from testModel.models import JugadaTest

class JugadaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'roll_string', 'user', 'played_date')
        model = JugadaTest