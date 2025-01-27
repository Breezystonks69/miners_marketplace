from django.test import TestCase

# Create your tests here.
from django.shortcuts import render
from .models import Miner

def index(request):
    miners = Miner.objects.all()
    return render(request, 'marketplace/index.html', {'miners': miners})