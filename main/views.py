from django.http import HttpResponse
from django.shortcuts import render

import random

def index(request):
    a = random.randint(1, 1001)
    b = random.randint(1, 1001)
    context = {'a': a, 'b': b}
    return render(request, 'index.html', context)
