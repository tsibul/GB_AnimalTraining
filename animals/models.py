from django.db import models
import datetime


# Create your models here.
class AnimalType(models.Model):
    type_name = models.CharField(max_length=140, null=False, blank=False)
    type_attribute = models.CharField(max_length=140, null=False, blank=False)

    def __repr__(self):
        return self.type_name

    def __str__(self):
        return self.type_name


class AnimalSpecies(models.Model):
    specie_name = models.CharField(max_length=140, null=False, blank=False)
    specie_attribute = models.CharField(max_length=140, null=False, blank=False)
    animal_type = models.ForeignKey(AnimalType, models.SET_NULL, null=True)

    def __repr__(self):
        return self.specie_name

    def __str__(self):
        return self.specie_name


class Commands(models.Model):
    command_name = models.CharField(max_length=140, null=False, blank=False)
    animal_type = models.ForeignKey(AnimalType, models.SET_NULL, null=True)

    def __repr__(self):
        return self.command_name

    def __str__(self):
        return self.command_name


class Animals(models.Model):
    animal_name = models.CharField(max_length=140, null=False, blank=False)
    date_birth = models.DateField(default='2023-01-01')
    animal_spec = models.ForeignKey(AnimalSpecies, models.SET_NULL, null=True)
    spec_attribute_value = models.CharField(max_length=140, default="")
    type_attribute_value = models.IntegerField(default=0)

    def animal_age_months(self):
        end = datetime.date.today()
        months = (end.year - self.date_birth.year) * 12 + (end.month - self.date_birth.month)
        if end.day >= self.date_birth.day:
            months += 1
        return months

    def training_list(self):
        commands = Training.objects.filter(animal=self).values_list('command', flat=True).order_by('command')
        command_list = Commands.objects.filter(id__in=commands).values_list('command_name', flat=True)
        command_list = '' if command_list.count() == 0 else ' | '.join(command_list)
        return command_list

    def __repr__(self):
        return self.animal_spec.specie_name + ' ' + self.animal_name + ' ' + \
            str(self.animal_age_months()) + 'месяцев'

    def __str__(self):
        return self.animal_spec.specie_name + ' ' + self.animal_name + ' ' + \
            str(self.animal_age_months()) + 'месяцев'


class Training(models.Model):
    command = models.ForeignKey(Commands, on_delete=models.CASCADE, null=False)
    animal = models.ForeignKey(Animals, on_delete=models.CASCADE, null=False)

    def __repr__(self):
        return self.animal.animal_name + ' ' + self.command.command_name

    def __str__(self):
        return self.animal.animal_name + ' ' + self.command.command_name


class Counter(models.Model):
    counter = models.IntegerField(default=0)
    animal = models.ForeignKey(Animals, models.SET_NULL, null=True)
    date = models.DateField(default='2023-07-01')
