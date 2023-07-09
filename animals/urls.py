from django.urls import path
from . import views

app_name = 'animals'

urlpatterns = [
#    path('/', views.maket_base, name='maket_base'),
    path('animal_types', views.animal_types, name='animal_types'),
    path('add_animal_type', views.add_animal_type, name='add_animal_type'),
    path('delete_type/<int:type_id>', views.delete_type, name='delete_type'),
]