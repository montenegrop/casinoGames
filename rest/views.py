from rest_framework.decorators import api_view
from rest_framework.response import Response

import json


f = open("rest/dummy_data/dama_muerta_1.json", "r")
data = json.load(f)
f.close()


@api_view()
def dummy_casino_json(request):
    return Response(data)