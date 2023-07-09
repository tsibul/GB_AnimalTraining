from animals.models import Training


def train_animal(animal, command):
    if not Training.objects.get(command=command, animal=animal):
        training = Training(command=command, animal=animal)
        training.save()
