from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from animals.models import AnimalType, Commands


def commands(request, type_id):
    navi = 'settings'
    animal_type_list = AnimalType.objects.all().order_by('type_name')
    if type_id == 0:
        command_list = Commands.objects.all().order_by('command_name')
    else:
        command_list = Commands.objects.filter(animal_type=type_id).order_by('command_name')
    context = {'navi': navi, 'animal_types': animal_type_list, 'type_id': type_id, 'command_list': command_list}
    return render(request, 'commands.html', context)


def add_command(request, type_id):
    spec = request.POST['spec']
    spec_id = request.POST['spec_id']
    try:
        command = Commands.objects.get(id=spec_id)
        command.command_name = spec
    except:
        command = Commands(command_name=spec)
    try:
        animal_type = AnimalType.objects.get(id=request.POST['type'])
        command.animal_type = animal_type
    except:
        pass
    command.save()
    return HttpResponseRedirect(reverse('animals:commands', args=(type_id,)))


def delete_command(request, type_id, com_id):
    command = Commands.objects.get(id=com_id)
    command.delete()
    return HttpResponseRedirect(reverse('animals:commands', args=(type_id,)))
