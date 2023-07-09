from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from animals.models import AnimalType


def animal_types(request):
    navi = 'settings'
    animal_type_list = AnimalType.objects.all().order_by('type_name')
    context = {'navi': navi, 'animal_types': animal_type_list}
    return render(request, 'animal_types.html', context)


def add_animal_type(request):
    animal_type = request.POST['type']
    type_attribute = request.POST['attribute']
    type_id = request.POST['type_id']
    try:
        animal_type_obj = AnimalType.objects.get(id=type_id)
        animal_type_obj.type_name = animal_type
    except:
        animal_type_obj = AnimalType(type_name=animal_type)
    animal_type_obj.type_attribute = type_attribute
    animal_type_obj.save()
    return HttpResponseRedirect(reverse('animals:animal_types'))


def delete_type(request, type_id):
    animal_type = AnimalType.objects.get(id=type_id)
    animal_type.delete()
    return HttpResponseRedirect(reverse('animals:animal_types'))
