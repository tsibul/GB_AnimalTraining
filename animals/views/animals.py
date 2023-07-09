from datetime import date, datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from animals.models import AnimalType, AnimalSpecies, Animals


def animals(request, type_id, spec_id):
    navi = 'animals'
    animal_type_list = AnimalType.objects.all().order_by('type_name')
    animal_specie_list = AnimalSpecies.objects.all().order_by('specie_name')
    if spec_id != 0:
        type_id = 0
        animal_list = Animals.objects.filter(animal_spec__id=spec_id).order_by('animal_name')
    elif type_id != 0:
        animal_list = Animals.objects.filter(animal_spec__animal_type__id=type_id).order_by('animal_name')
    else:
        animal_list = Animals.objects.all().order_by('animal_name')

    context = {'navi': navi, 'animal_types': animal_type_list, 'animal_specs': animal_specie_list, 'type_id': type_id,
               'animals': animal_list, 'spec_id': spec_id}
    return render(request, 'index.html', context)


def add_animal(request, type_id, spec_id):
    animal_spec = AnimalSpecies.objects.get(id=request.POST['spec'])
    spec_attr = request.POST['spec_attr']
    type_attr = request.POST['type_attr']
    date_birth = datetime.strptime(request.POST['date'], '%Y-%m-%d')
    name = request.POST['name']
    animal_id = request.POST['spec_id']
    try:
        animal = Animals.objects.get(id=animal_id)
        animal.animal_name = name
    except:
        animal = Animals(animal_name=name)
        animal.animal_spec = animal_spec
        animal.date_birth = date_birth
        animal.spec_attribute_value = spec_attr
        animal.type_attribute_value = type_attr
        animal.save()
    return HttpResponseRedirect(reverse('animals:animals', args=(type_id, spec_id)))


def delete_animal(request, type_id, spec_id, animal_id):
    animal = Animals.objects.get(id=animal_id)
    animal.delete()
    return HttpResponseRedirect(reverse('animals:animals', args=(type_id, spec_id)))
