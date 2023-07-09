from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from animals.models import AnimalType, AnimalSpecies


def animal_species(request, type_id):
    navi = 'settings'
    if type_id == 0:
        animal_type_list = AnimalType.objects.all().order_by('type_name')
        animal_specie_list = AnimalSpecies.objects.all().order_by('specie_name')
    else:
        animal_type_list = AnimalType.objects.get(id=type_id)
        animal_specie_list = AnimalSpecies.objects.filter(animal_type=animal_type_list).order_by('specie_name')
    context = {'navi': navi, 'animal_types': animal_type_list, 'animal_species': animal_specie_list, 'type_id': type_id}
    return render(request, 'animal_species.html', context)


def add_animal_species(request, type_id):
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
    return HttpResponseRedirect(reverse('animals:animal_species', args=type_id))


def delete_type(request, type_id):
    animal_type = AnimalType.objects.get(id=type_id)
    animal_type.delete()
    return HttpResponseRedirect(reverse('animals:animal_types', args=type_id))
