import json
from django.db.models import Q
from django.http import JsonResponse
from animals.models import Animals, Commands
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

from django.core.serializers import serialize
from django.utils.encoding import force_str


def get_data_as_json(animal_id, param):
    if not param:
        animal = Animals.objects.get(id=animal_id)
        data = Commands.objects.filter(
            ~Q(training__animal=animal) &
            (Q(animal_type=None) | Q(animal_type=animal.animal_spec.animal_type)))
    else:
        data = Commands.objects.filter(training__animal_id=animal_id)
    json_data = serialize('python', data)
    json_data = json.dumps(json_data, ensure_ascii=False)

    return json_data


def json_view(request, animal_id, param):
    json_data = get_data_as_json(animal_id, param)  # Предполагается, что у вас есть функция get_data_as_json()
    return JsonResponse(json_data, safe=False)
