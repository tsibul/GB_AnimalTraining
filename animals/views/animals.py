from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from animals.models import AnimalType, AnimalSpecies, Animals


def animals(request, type_id, spec_id):
    navi = 'animals'
    animal_type_list = AnimalType.objects.all().order_by('type_name')
    animal_specie_list = AnimalSpecies.objects.all().order_by('specie_name')
    if type_id == 0 and spec_id == 0:
        animal_list = Animals.objects.all().order_by('animal_name')
    elif spec_id == 0:
        animal_list = Animals.objects.filter(animal_spec__animal_type__id=type_id).order_by('animal_name')
    else:
        type_id = 0
        animal_list = Animals.objects.filter(animal_spec__id=spec_id).order_by('animal_name')
    context = {'navi': navi, 'animal_types': animal_type_list, 'animal_specs': animal_specie_list, 'type_id': type_id,
               'animals': animal_list, 'spec_id': spec_id}
    return render(request, 'index.html', context)


def add_animal(request, type_id, spec_id):
    animal_type = AnimalType.objects.get(id=request.POST['type'])
    animal_spec = request.POST['spec']
    spec_attribute = request.POST['attribute']
    spec_id = request.POST['spec_id']
    try:
        animal_spec_obj = AnimalSpecies.objects.get(id=spec_id)
        animal_spec_obj.specie_name = animal_spec
    except:
        animal_spec_obj = AnimalSpecies(specie_name=animal_spec)
    animal_spec_obj.specie_attribute = spec_attribute
    animal_spec_obj.animal_type = animal_type
    animal_spec_obj.save()
    return HttpResponseRedirect(reverse('animals:animals', args=(type_id, spec_id)))


def delete_animal(request, type_id, spec_id):
    animal_spec = AnimalSpecies.objects.get(id=spec_id)
    animal_spec.delete()
    return HttpResponseRedirect(reverse('animals:animals', args=(type_id, spec_id)))
