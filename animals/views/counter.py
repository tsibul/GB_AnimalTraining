from django.db.models import Max
from django.shortcuts import render

from animals.models import Counter


def counter_list(request):
    navi = 'counter'
    max_count = Counter.objects.aggregate(max_counter=Max('counter'))
    max_count = max_count['max_counter']
    counter = Counter.objects.all().order_by('-date')
    context = {'max_count': max_count, 'counter': counter, 'navi': navi}
    return render(request, 'counter.html', context)
