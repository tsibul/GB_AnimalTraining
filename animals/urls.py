from django.urls import path
from . import views

app_name = 'animals'

urlpatterns = [
    path('<int:type_id>/<int:spec_id>', views.animals, name='animals'),
    path('add_animal/<int:type_id>/<int:spec_id>', views.add_animal, name='add_animal'),
    path('delete_animal/<int:type_id>/<int:spec_id>/<int:animal_id>', views.delete_animal, name='delete_animal'),

    path('animal_types', views.animal_types, name='animal_types'),
    path('add_animal_type', views.add_animal_type, name='add_animal_type'),
    path('delete_type/<int:type_id>', views.delete_type, name='delete_type'),

    path('add_animal_spec/<int:type_id>', views.add_animal_species, name='add_animal_species'),
    path('animal_species/<int:type_id>', views.animal_species, name='animal_species'),
    path('delete_spec/<int:type_id>/<int:spec_id>', views.delete_specie, name='delete_specie'),

    path('commands/<int:type_id>', views.commands, name='commands'),
    path('add_command/<int:type_id>', views.add_command, name='add_command'),
    path('delete_command/<int:type_id>/<int:com_id>', views.delete_command, name='delete_command'),

    path('training/<int:type_id>/<int:com_id>', views.training, name='training'),

]