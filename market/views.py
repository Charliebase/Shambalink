from django.shortcuts import render
from .models import Produce

def produce_list(request):
    produce = Produce.objects.all().order_by('-posted_on')
    return render(request, 'produce_list.html', {'produce': produce})
