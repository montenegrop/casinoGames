from rest_framework.decorators import api_view
from rest_framework.response import Response

import json
from machine.computations.random_numbers import random_integer
from machine.computations.examples.victorious_payment import payment


f = open("rest/dummy_data/dama_muerta_1.json", "r")
data = json.load(f)
f.close()


@api_view()
def dummy_casino_json(request):
    return Response(data)


@api_view()
def dummy_victorious_json(request):
    roll = []
    for num in range(0, 5):
        roll.append(random_integer(0, 8))

    result = payment(roll=roll, bet=1)
    data = result
    return Response(data)


@api_view()
def realistic_victorious_json(request):
    roll = []
    for num in range(0, 5):
        roll.append(random_integer(0, 8))

    result = payment(roll=roll, bet=1)
    data = result
    return Response(data)
