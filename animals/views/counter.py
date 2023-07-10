from django.db.models import Max
from django.shortcuts import render

from animals.models import Counter


def counter_list(request):
    max_count = Counter.objects.aggregate(Max('counter'))
    counter = Counter.objects.all().order_by('-date')
    context = {'max_count': max_count, 'counter': counter}
    return render(request, 'counter.html', context)